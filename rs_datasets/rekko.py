import json
import logging
from os import rename
from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class Rekko(Dataset):
    def __init__(self, path: str = None):
        super().__init__(path)
        folder = join(self.data_folder, 'rekko')
        if not exists(folder):
            self._download(folder)

        self.transactions = dt.fread(
            join(folder, 'transactions.csv'),
            columns=[
                'item_id', 'user_id', 'consumption_mode', 'ts',
                'watched_time', 'device_type', 'device_manufacturer'
            ],
        ).to_pandas()

        self.ratings = dt.fread(
            join(folder, 'ratings.csv'),
            columns=['user_id', 'item_id', 'rating', 'ts']
        ).to_pandas()

        self.bookmarks = dt.fread(
            join(folder, 'bookmarks.csv'),
            columns=['user_id', 'item_id', 'ts']
        ).to_pandas()

        with open(join(folder, 'catalogue.json')) as json_file:
            self.catalogue = json.load(json_file)


    @safe
    def _download(self, path):
        logging.info('Downloading rekko challenge dataset...')
        archive = 'rekko_challenge_rekko_challenge_2019.zip'
        url = f'https://boosters.pro/api/ch/files/pub/{archive}'
        download_dataset(url, join(self.data_folder, 'rekko.zip'))
        rename(join(self.data_folder, 'rekko'), path)
