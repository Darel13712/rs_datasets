from os import mkdir, rename
from os.path import join, exists

import pandas as pd
import numpy as np

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class Jester(Dataset):
    def __init__(self, dataset: int = 1, path: str = None):
        """
        :param dataset: version of dataset (1, 3, 4).
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        if dataset not in {1, 3, 4}:
            raise ValueError('Dataset version must be one of {1, 3, 4}')
        folder = join(self.data_folder, 'jester')
        if not exists(folder):
            self._download(folder)

        if dataset == 1:
            data = []
            for i in [1, 2, 3]:
                ratings = pd.read_excel(join(folder, str(dataset), f'data_{i}.xls'), header=None)
                ratings = self._process(ratings)
                data.append(ratings)
            self.data1 = data[0]
            self.data2 = data[1]
            self.data3 = data[2]
            jokes = pd.read_excel(join(folder, '3', f'jokes.xlsx'), header=None)
            self.jokes = self._fix_jokes(jokes)
        else:
            data = pd.read_excel(join(folder, str(dataset), f'data.xlsx'), header=None)
            self.data = self._process(data)
            jokes = pd.read_excel(join(folder, str(dataset), f'jokes.xlsx'), header=None)
            self.jokes = self._fix_jokes(jokes)

    @staticmethod
    def _process(df):
        df = df.drop(0, axis=1)
        df = df.replace(99, np.nan)
        df = df.astype(pd.SparseDtype('float', np.nan))
        return df

    @staticmethod
    def _fix_jokes(df):
        df.index = range(1, len(df) + 1)
        return df[0]

    @safe
    def _download(self, path):
        self.logger.info('Downloading Jester dataset...')
        mkdir(path)
        base_url = 'http://eigentaste.berkeley.edu/dataset/'

        self.logger.info('Dataset 1...')
        d1 = join(path, '1')
        mkdir(d1)
        download_dataset(
            base_url + 'jester_dataset_1_joke_texts.zip',
            join(d1, 'joke_texts.zip'),
            manage_folder=False
        )
        for i in [1, 2, 3]:
            download_dataset(
                base_url + f'jester_dataset_1_{i}.zip',
                join(d1, f'ratings_{i}.zip'),
                manage_folder=False
            )
            rename(join(d1, f'jester-data-{i}.xls'), join(d1, f'data_{i}.xls'))

        for i in [3, 4]:
            self.logger.info(f'Dataset {i}...')
            d = join(path, str(i))
            mkdir(d)
            download_dataset(
                base_url + f'Dataset{i}JokeSet.zip',
                join(d, 'joke_texts.zip'),
                manage_folder=False
            )
            rename(join(d, f'Dataset{i}JokeSet.xlsx'), join(d, 'jokes.xlsx'))
            download_dataset(
                base_url + f'JesterDataset{i}.zip',
                join(d, 'ratings.zip'),
                manage_folder=False
            )
            if i == 3:
                name = 'FINAL jester 2006-15.xls'
            else:
                name = '[final] April 2015 to Nov 30 2019 - Transformed Jester Data - .xlsx'
            rename(join(d, name), join(d, 'data.xlsx'))
