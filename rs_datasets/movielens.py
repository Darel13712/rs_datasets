import os
from os import rename
from os.path import join
from typing import Tuple

import datatable as dt
from datatable import Frame

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe

rating_cols = ['user_id', 'item_id', 'rating', 'timestamp']
item_cols = ['item_id', 'title', 'genres']
tag_cols = ['user_id', 'item_id', 'tag', 'timestamp']
user_cols = ['user_id', 'gender', 'age', 'occupation', 'zip_code']
link_cols = ['item_id', 'imdb_id', 'tmdb_id']
tag_g_cols = ['tag_id', 'tag']
score_cols = ['movie_id', 'tag_id', 'rating']
genre_cols = ['item_id', 'title', 'release_date', 'video_release_date',
              'imdb_url', 'unknown', 'Action', 'Adventure', 'Animation',
              'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama',
              'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
              'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

class MovieLens(Dataset):
    def __init__(
            self,
            version: str = 'small',
            read_genome: bool = False,
            path: str = None
    ):
        """
        :param version: dataset version,
            one of {'100k', '1m', '10m', '20m', '25m', 'small', 'latest'}
        :param read_genome: whether to read genome tag dataset or not
            (available from version 20m and up).
            Are not loaded by default to save memory.
        :param path: where to read dataset from or where to download to.
        """
        super().__init__(path)
        options = {'100k', '1m', '10m', '20m', '25m', 'small', 'latest'}
        if version not in options:
            raise ValueError(
                f'{version} is not supported. Available options: {options}')

        if version == 'small':
            dataset = 'ml-latest-small'
        else:
            dataset = 'ml-' + version

        folder = join(self.data_folder, dataset)
        if not os.path.exists(folder):
            self._download(folder, dataset)
        
        if version == '100k':
            (self.ratings,
             self.users,
             self.items) = self._read_100k(folder)
        elif version == '1m':
            (self.ratings,
             self.users,
             self.items) = self._read_1m(folder)
        elif version == '10m':
            (self.ratings,
             self.items,
             self.tags) = self._read_10m(folder)
        else:
            (self.ratings,
             self.items,
             self.tags,
             self.links) = self._read_modern(folder)
            if read_genome:
                (self.genome_tags,
                 self.genome_scores) = self._read_genome(folder)

    @staticmethod
    def _read_modern(folder: str) -> Tuple[Frame, Frame, Frame, Frame]:
        ratings = dt.fread(join(folder, 'ratings.csv'), columns=rating_cols).to_pandas()
        items = dt.fread(join(folder, 'movies.csv'), columns=item_cols).to_pandas()
        tags = dt.fread(join(folder, 'tags.csv'), columns=tag_cols).to_pandas()
        links = dt.fread(join(folder, 'links.csv'), columns=link_cols).to_pandas()
        return ratings, items, tags, links

    @staticmethod
    def _read_genome(folder: str) -> Tuple[Frame, Frame]:
        genome_tags = dt.fread(join(folder, 'genome-tags.csv'), columns=tag_g_cols).to_pandas()
        genome_scores = dt.fread(join(folder, 'genome-scores.csv'), columns=score_cols).to_pandas()
        return genome_tags, genome_scores

    @staticmethod
    def _read_10m(folder: str) -> Tuple[Frame, Frame, Frame]:
        ratings = dt.fread(join(folder, 'ratings.dat'), columns=rating_cols).to_pandas()
        items = dt.fread(join(folder, 'movies.dat'), columns=item_cols).to_pandas()
        tags = dt.fread(join(folder, 'tags.dat'), columns=tag_cols).to_pandas()
        return ratings, items, tags

    @staticmethod
    def _read_1m(folder: str) -> Tuple[Frame, Frame, Frame]:
        ratings = dt.fread(join(folder, 'ratings.dat'), columns=rating_cols).to_pandas()
        users = dt.fread(join(folder, 'users.dat'), columns=user_cols).to_pandas()
        items = dt.fread(join(folder, 'movies.dat'), columns=item_cols).to_pandas()
        return ratings, users, items

    @staticmethod
    def _read_100k(folder: str) -> Tuple[Frame, Frame, Frame]:
        ratings = dt.fread(join(folder, 'u.data'), columns=rating_cols).to_pandas()
        users = dt.fread(join(folder, 'u.user'), columns=user_cols).to_pandas()
        items = dt.fread(join(folder, 'u.item'), columns=genre_cols)
        del items[:, 'video_release_date']
        items = items.to_pandas()
        return ratings, users, items

    @safe
    def _download(self, path, dataset):
        """
        Download data from https://grouplens.org/datasets/movielens/
        Available options: ml-20m, ml-latest-small, ml-latest and other,
        can be checked on ml site.

        :param path: where to save
        :param dataset: dataset version
        :return: None
        """
        self.logger.info('Downloading %s from grouplens...', dataset)
        archive = dataset + '.zip'
        url = f'http://files.grouplens.org/datasets/movielens/{archive}'
        download_dataset(url, path + '.zip')
        if dataset == 'ml-10m':
            rename(join(self.data_folder, 'ml-10M100K'), path)
            self.replace_separator(join(path, 'movies.dat'), '::', '\t')
            self.replace_separator(join(path, 'ratings.dat'), '::', '\t')
            self.replace_separator(join(path, 'tags.dat'), '::', '\t')
        elif dataset == 'ml-1m':
            self.replace_separator(join(path, 'movies.dat'), '::', '\t', 'ISO-8859-1')
            self.replace_separator(join(path, 'ratings.dat'), '::', '\t')
            self.replace_separator(join(path, 'users.dat'), '::', '\t')

    @staticmethod
    def replace_separator(filepath: str, old: str, new: str, encoding: str = 'utf8'):
        with open(filepath, 'r', encoding=encoding) as f:
            newlines = []
            for line in f.readlines():
                newlines.append(line.replace(old, new))
        with open(filepath, 'w') as f:
            for line in newlines:
                f.write(line)
