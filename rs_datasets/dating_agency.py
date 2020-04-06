from os import rename
from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class DatingAgency(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'dating_agency')
        if not exists(folder):
            self._download(folder)

        self.ratings = dt.fread(
            join(folder, 'ratings.dat'),
            columns=['user_id', 'profile_id', 'rating']
        ).to_pandas()

        self.users = dt.fread(
            join(folder, 'gender.dat'),
            columns=['user_id', 'gender']
        ).to_pandas()

    @safe
    def _download(self, path):
        self.logger.info('Downloading Dating Agency Dataset...')
        url = 'http://www.occamslab.com/petricek/data/libimseti-complete.zip'
        download_dataset(url, join(self.data_folder, 'dating.zip'))
        rename(join(self.data_folder, 'libimseti'), path)
