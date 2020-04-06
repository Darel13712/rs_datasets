from os import mkdir
from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class Epinions(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'epinions')
        if not exists(folder):
            self._download(folder)

        self.ratings = dt.fread(
            join(folder, 'ratings_data.txt'),
            columns=['user_id', 'item_id', 'rating']
        ).to_pandas()

        self.trust = dt.fread(
            join(folder, 'trust_data.txt'),
            columns=['source_user_id', 'target_user_id', 'trust_value']
        ).to_pandas()

    @safe
    def _download(self, path):
        self.logger.info('Downloading Epinions dataset...')
        mkdir(path)
        base_url = 'http://www.trustlet.org/datasets/downloaded_epinions/'

        filepath = join(path, 'ratings_data.txt.bz2')
        download_dataset(
            base_url + 'ratings_data.txt.bz2',
            filepath,
            manage_folder=False
        )

        filepath = join(path, 'trust_data.txt.bz2')
        download_dataset(
            base_url + 'trust_data.txt.bz2',
            filepath,
            manage_folder=False
        )
