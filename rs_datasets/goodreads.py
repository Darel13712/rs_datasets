from os import mkdir
from os.path import join, exists

import datatable as dt
import gdown

from rs_datasets.generic_dataset import Dataset, safe


class Goodreads(Dataset):
    def __init__(self, path: str = None, read_maps: bool = False):
        """
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        :param read_maps: ids in interactions are encoded to save memory.
            You can read mappings, but there's no point
            if you don't use the rest of the dataset, which is not included here.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'goodreads')
        if not exists(folder):
            self._download(folder)

        self.ratings = dt.fread(
            join(folder, 'goodreads_interactions.csv'),
            columns=['user_id', 'item_id', 'is_read', 'rating', 'is_reviewed']
        ).to_pandas()

        if read_maps:
            self.books = dt.fread(
                join(folder, 'book_id_map.csv')
            ).to_pandas()

            self.users = dt.fread(
                join(folder, 'user_id_map.csv')
            ).to_pandas()

    @safe
    def _download(self, path):
        """
        https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/shelves
        https://github.com/MengtingWan/goodreads/blob/master/download.ipynb
        """
        self.logger.info('Downloading interactions from Goodreads dataset...')
        mkdir(path)

        gdrive = 'https://drive.google.com/uc?id='
        interactions = gdrive + '1zmylV7XW2dfQVCLeg1LbllfQtHD2KUon'
        users = gdrive + '15ax-h0Oi_Oyee8gY_aAQN6odoijmiz6Q'
        items = gdrive + '1CHTAaNwyzvbi1TR08MJrJ03BxA266Yxr'

        gdown.download(users, join(path, 'user_id_map.csv'))
        gdown.download(items, join(path, 'book_id_map.csv'))
        gdown.download(interactions, join(path, 'goodreads_interactions.csv'))
