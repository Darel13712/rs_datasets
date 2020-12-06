import os
from os.path import join, exists

import datatable as dt
import gdown

from rs_datasets.data_loader import extract
from rs_datasets.generic_dataset import Dataset, safe


class Diginetica(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'diginetica')
        if not exists(folder):
            self._download(folder)

        self.items = dt.fread(
            join(folder, 'products.csv'),
            columns=['item_id', 'log2price', 'name_tokens']
        ).to_pandas()

        self.categories = dt.fread(
            join(folder, 'product-categories.csv'),
            columns=['item_id', 'category_id']
        ).to_pandas()

        self.purchases = dt.fread(
            join(folder, 'train-purchases.csv'),
            columns=['session_id', 'user_id', 'timeframe', 'date', 'order_id', 'item_id']
        ).to_pandas()

        self.views = dt.fread(
            join(folder, 'train-item-views.csv'),
            columns=['session_id', 'user_id', 'item_id', 'timeframe', 'date']
        ).to_pandas()

        self.queries = dt.fread(
            join(folder, 'train-queries.csv'),
            columns=['query_id', 'session_id', 'user_id', 'timeframe', 'duration', 'date',
                     'tokens', 'category_id', 'items', 'is_test']
        ).to_pandas()



    @safe
    def _download(self, path):
        self.logger.info('Downloading Diginetica Dataset...')
        url = 'https://drive.google.com/uc?id=0B7XZSACQf0KdenRmMk8yVUU5LWc'
        zip = join(self.data_folder, 'diginetica.zip')
        gdown.download(url, zip)
        extract(zip)
        os.remove(zip)
