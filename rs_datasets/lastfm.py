from os import rename
from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class Lastfm(Dataset):
    def __init__(self, path: str = None):
        super().__init__(path)
        folder = join(self.data_folder, 'lastfm')
        if not exists(folder):
            self._download(folder)

        self.play_counts = dt.fread(
            join(folder, 'usersha1-artmbid-artname-plays.tsv'),
            columns=['user_id', 'artist_id', 'artist_name', 'play_count']
        ).to_pandas()

        self.users = dt.fread(
            join(folder, 'usersha1-profile.tsv'),
            columns=['user_id', 'gender', 'age', 'country', 'signup_date']
        ).to_pandas()

    @safe
    def _download(self, path):
        self.logger.info('Downloading Last.fm 360k dataset...')
        url = 'http://mtg.upf.edu/static/datasets/last.fm/lastfm-dataset-360K.tar.gz'
        download_dataset(url, join(self.data_folder, 'lastfm.tar.gz'))
        rename(join(self.data_folder, 'lastfm-dataset-360K'), path)
