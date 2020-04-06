from glob import glob
from os import mkdir, remove, rename
from os.path import exists, join

import datatable as dt
import pandas as pd
from tqdm import tqdm

from rs_datasets.data_loader import download_dataset, extract, rm_if_exists
from rs_datasets.generic_dataset import Dataset, safe


class Netflix(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: where to read dataset from or where to download to.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'netflix')
        if not exists(folder):
            self._download(folder)
            self._save_clean(folder)
        self._read_clean(folder)

    def _read_clean(self, folder):
        path = join(folder, 'clean')
        self.movies = pd.read_csv(join(path, 'movies.csv'), sep='\t',
                                  names=['item_id', 'year', 'title'],
                                  dtype={'item_id': 'uint16',
                                         'year': 'float32'})
        test = dt.fread(
            join(path, 'test.csv'),
            columns=['item_id', 'user_id', 'timestamp']
        ).to_pandas()
        test['timestamp'] = pd.to_datetime(test['timestamp'])
        test['user_id'] = test['user_id'].astype('category')
        test['item_id'] = test['item_id'].astype('category')
        self.test = test

        if exists(join(path, 'train.parquet')):
            self.train = pd.read_parquet(join(path, 'train.parquet'))
        else:
            train = dt.fread(
                join(path, 'train.csv'),
                columns=['item_id', 'user_id', 'rating', 'timestamp']
            ).to_pandas()
            train['timestamp'] = pd.to_datetime(train['timestamp'])
            train['rating'] = train['rating'].astype('uint8')
            train['user_id'] = train['user_id'].astype('category')
            train['item_id'] = train['item_id'].astype('category')
            self.train = train
            self.train.to_parquet(join(path, 'train.parquet'))
            remove(join(path, 'train.csv'))

    def _save_clean(self, raw):
        clean = join(raw, 'clean')
        mkdir(clean)
        self._fix_movies(raw, clean)
        self._fix_train(raw, clean)
        self._fix_test(raw, clean)

    @staticmethod
    def _fix_test(raw, clean):
        dest = open(join(clean, 'test.csv'), 'w')
        with open(join(raw, 'qualifying.txt')) as source:
            for line in source:
                if line[-2] == ':':
                    movie_id = line[:-2] + ','
                else:
                    dest.write(movie_id + line)
        dest.close()

    def _fix_train(self, raw, clean):
        self.logger.info('Parsing train files')
        folder = join(raw, 'training_set')
        files = glob(join(folder, '*.txt'))
        dest = open(join(clean, 'train.csv'), 'w')
        for file in tqdm(files):
            with open(file) as source:
                for line in source:
                    if line[-2] == ':':
                        movie_id = line[:-2] + ','
                    else:
                        dest.write(movie_id + line)
        dest.close()

    @staticmethod
    def _fix_movies(raw, clean):
        """
        Comma separator also appears in movie titles, for example:
        `72,1974,At Home Among Strangers, A Stranger Among His Own`
        Separator is changed to tabulation for easy parsing.
        """
        file = join(raw, 'movie_titles.txt')
        dest = open(join(clean, 'movies.csv'), 'w')
        with open(file, encoding='ISO-8859-1') as f:
            for line in f.readlines():
                first = line.find(',')
                second = first + 5
                m_id = line[:first]
                year = line[first + 1:second]
                title = line[second + 1:]
                dest.write('\t'.join([m_id, year, title]) + '\n')
        dest.close()

    @safe
    def _download(self, path):
        self.logger.info('Downloading Netflix Prize dataset...')
        url = 'https://archive.org/download/nf_prize_dataset.tar/nf_prize_dataset.tar.gz'
        download_dataset(url, join(self.data_folder, 'netflix.tar.gz'))
        rename(join(self.data_folder, 'download'), path)
        archive = join(path, 'training_set.tar')
        extract(archive)
        rm_if_exists(archive)
