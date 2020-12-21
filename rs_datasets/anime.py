import logging
from os.path import join, exists

import datatable as dt

from rs_datasets.generic_dataset import Dataset, safe


class Anime(Dataset):
    def __init__(self, path: str = None):
        super().__init__(path)
        folder = join(self.data_folder, 'anime')
        if not exists(folder):
            self._download(folder)

        self.ratings = dt.fread(
            join(folder, 'rating.csv'),
            columns=[
                'user_id', 'item_id', 'rating'
            ],
        ).to_pandas()

        self.titles = dt.fread(
            join(folder, 'anime.csv'),
            columns=[
                'item_id', 'name', 'genre', 'type', 'episodes', 'rating', 'members'
            ],
        ).to_pandas()

    @safe
    def _download(self, path):
        from kaggle.api.kaggle_api_extended import KaggleApi
        logging.info('Downloading anime dataset...')
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files('CooperUnion/anime-recommendations-database', path, unzip=True)
