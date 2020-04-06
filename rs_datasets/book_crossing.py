from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_dataset
from rs_datasets.generic_dataset import Dataset, safe


class BookCrossing(Dataset):
    def __init__(self, path: str = None):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'bookx')
        if not exists(folder):
            self._download(folder)

        self.ratings = dt.fread(
            join(folder, 'BX-Book-Ratings.csv'),
            columns=['user_id', 'item_id', 'rating']
        ).to_pandas()

        self.items = dt.fread(
            join(folder, 'BX-Books.csv'),
            columns=['item_id', 'title', 'author', 'year',
                     'publisher', 'img_s', 'img_m', 'img_l']
        ).to_pandas()

        users = dt.fread(
            join(folder, 'BX-Users.csv'),
            columns=['user_id', 'location', 'age']
        ).to_pandas()

        users['age'] = users['age'].replace("NULL", "nan").astype('float')
        self.users = users

    @safe
    def _download(self, path):
        self.logger.info('Downloading Book-Crossing Dataset...')
        url = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'
        download_dataset(url, join(self.data_folder, 'bookx.zip'))
