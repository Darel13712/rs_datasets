import logging
from os.path import join, exists

import datatable as dt

from rs_datasets.generic_dataset import Dataset, safe


class Steam(Dataset):
    def __init__(self, path: str = None):
        super().__init__(path)
        folder = join(self.data_folder, 'steam')
        if not exists(folder):
            self._download(folder)

        self.data = dt.fread(
            join(folder, 'steam-200k.csv'),
            columns=[
                'user_id', 'game', 'behavior', 'value', 'c'
            ],
        ).to_pandas()
        self.data = self.data.drop('c', axis=1)

    @safe
    def _download(self, path):
        from kaggle.api.kaggle_api_extended import KaggleApi
        logging.info('Downloading steam dataset...')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files('tamber/steam-video-games', path, unzip=True)
