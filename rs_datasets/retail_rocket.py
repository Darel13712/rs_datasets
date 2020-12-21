import logging
from os.path import join, exists

import datatable as dt

from rs_datasets.generic_dataset import Dataset, safe


class RetailRocket(Dataset):
    def __init__(self, path: str = None):
        super().__init__(path)
        folder = join(self.data_folder, 'retail_rocket')
        if not exists(folder):
            self._download(folder)

        self.category_tree = dt.fread(
            join(folder, 'category_tree.csv'),
            columns=[
                'category_id', 'parent_id'
            ],
        ).to_pandas()

        self.log = dt.fread(
            join(folder, 'events.csv'),
            columns=[
                'ts', 'user_id', 'event', 'item_id', 'transaction_id'
            ],
        ).to_pandas()

        items1 = dt.fread(
            join(folder, 'item_properties_part1.csv'),
            columns=[
                'ts', 'item_id', 'property', 'value'
            ],
        ).to_pandas()

        items2 = dt.fread(
            join(folder, 'item_properties_part2.csv'),
            columns=[
                'ts', 'item_id', 'property', 'value'
            ],
        ).to_pandas()

        self.items = items1.append(items2, ignore_index=True)

    @safe
    def _download(self, path):
        from kaggle.api.kaggle_api_extended import KaggleApi
        logging.info('Downloading Retail Rocket dataset...')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files('retailrocket/ecommerce-dataset', path, unzip=True, quiet=False)
