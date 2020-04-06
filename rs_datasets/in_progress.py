import logging
from os import mkdir, rename
from os.path import  join

from rs_datasets.data_loader.loaders import download_dataset


def download_rekko(path: str = '.'):
    """
    Скачать датасет с rekko chalenge
    https://boosters.pro/championship/rekko_challenge/data
    175MB

    :param path: куда положить
    :return: None
    """
    logging.info('Downloading rekko challenge dataset...')
    archive = 'rekko_challenge_rekko_challenge_2019.zip'
    url = f'https://boosters.pro/api/ch/files/pub/{archive}'
    path = join(path, 'rekko.zip')
    download_dataset(url, path)


def download_citeulike_a(path: str = '.'):
    """
    Скачать CiteULike-a
    https://github.com/js05212/citeulike-a

    :param path: куда положить
    :return: None
    """
    logging.info('Downloading CiteULike-a dataset...')
    url = 'https://github.com/js05212/citeulike-a/archive/master.zip'
    download_dataset(url, join(path, 'citeulike-a.zip'))
    rename(join(path, 'citeulike-a-master'), join(path, 'citeulike-a'))


def download_hetrec(path: str = '.'):
    """
    Скачать HetRec 2011
    https://grouplens.org/datasets/hetrec-2011/

    :param path: куда положить
    :return: None
    """
    logging.info('Downloading HetRec 2011 dataset...')
    folder = join(path, 'hetrec')
    mkdir(folder)
    base_url = 'http://files.grouplens.org/datasets/hetrec2011/'

    download_dataset(
        base_url + 'hetrec2011-delicious-2k.zip',
        join(folder, 'delicious.zip')
    )
    download_dataset(
        base_url + 'hetrec2011-lastfm-2k.zip',
        join(folder, 'lastfm.zip')
    )
    download_dataset(
        base_url + 'hetrec2011-movielens-2k-v2.zip',
        join(folder, 'movielens.zip')
    )
