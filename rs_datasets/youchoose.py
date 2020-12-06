from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class YooChoose(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'yoochoose')
        if not exists(folder):
            self._download(folder)

        self.log = dt.fread(
            join(folder, 'yoochoose-clicks.dat'),
            columns=['session_id', 'ts', 'item_id', 'category']
        ).to_pandas()

        self.purchases = dt.fread(
            join(folder, 'yoochoose-buys.dat'),
            columns=['session_id', 'ts', 'item_id', 'price', 'quantity']
        ).to_pandas()

        self.test = dt.fread(
            join(folder, 'yoochoose-test.dat'),
            columns=['session_id', 'ts', 'item_id', 'category']
        ).to_pandas()


    @safe
    def _download(self, path):
        self.logger.info('Downloading YooChoose Dataset...')
        url = 'https://s3-eu-west-1.amazonaws.com/yc-rdata/yoochoose-data.7z'
        download_dataset(url, join(self.data_folder, 'yoochoose.7z'))
