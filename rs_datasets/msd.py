import os
from os import rename
from os.path import join

import datatable as dt
import pandas as pd

from rs_datasets.data_loader import download_dataset, download_url
from rs_datasets.generic_dataset import Dataset, safe


class MillionSongDataset(Dataset):
    def __init__(
            self,
            merge_kaggle_splits: bool = True,
            drop_mismatches: bool = True,
            path: str = None
    ):
        """
        :param merge_kaggle_splits:
            In MSD Challenge on [Kaggle](https://www.kaggle.com/c/msdchallenge) there were
            public and private parts. By default they are merged together. You can change this, setting
            `merge_kaggle_splits` to `False`.
        :param drop_mismatches:
            There is a [matching error](http://millionsongdataset.com/blog/12-2-12-fixing-matching-errors/)
            between track ids and song ids in MSD. It shouldn't matter if you don't use audio features, but
            by default these items are removed.
        :param path: where to read dataset from or where to download to.
        """
        super().__init__(path)
        folder = join(self.data_folder, 'msd')
        if not os.path.exists(folder):
            self._download(folder)

        try_cache = merge_kaggle_splits and drop_mismatches
        processed = join(folder, 'clean')
        if try_cache and os.path.exists(processed):
            self.train = dt.fread(join(processed, 'train.csv')).to_pandas()
            self.val = dt.fread(join(processed, 'val.csv')).to_pandas()
            self.test = dt.fread(join(processed, 'test.csv')).to_pandas()
        else:
            eval_folder = join(folder, 'evaluation')
            self.train = self._read_triplets(join(folder,
                                                  'train_triplets.txt'))
            val_vis = self._read_triplets(join(eval_folder,
                                               'year1_valid_triplets_visible.txt'))
            val_hid = self._read_triplets(join(eval_folder,
                                               'year1_valid_triplets_hidden.txt'))
            test_vis = self._read_triplets(join(eval_folder,
                                                'year1_test_triplets_visible.txt'))
            test_hid = self._read_triplets(join(eval_folder,
                                                'year1_test_triplets_hidden.txt'))
            if drop_mismatches:
                mismatches = self._read_mismatches(folder)
                mismatches = set(mismatches.item_id)
                self.train = self._drop_mismatches(self.train, mismatches)
                val_vis = self._drop_mismatches(val_vis, mismatches)
                val_hid = self._drop_mismatches(val_hid, mismatches)
                test_vis = self._drop_mismatches(test_vis, mismatches)
                test_hid = self._drop_mismatches(test_hid, mismatches)

            if merge_kaggle_splits:
                self.val = pd.concat([val_vis, val_hid], ignore_index=True)
                self.test = pd.concat([test_vis, test_hid], ignore_index=True)
            else:
                self.val_visible = val_vis
                self.val_hidden = val_hid
                self.test_visible = test_vis
                self.test_hidden = test_hid

            if try_cache and not os.path.exists(processed):
                os.mkdir(processed)
                self.train.to_csv(join(processed, 'train.csv'), index=False)
                self.val.to_csv(join(processed, 'val.csv'), index=False)
                self.test.to_csv(join(processed, 'test.csv'), index=False)

    @staticmethod
    def _read_triplets(path):
        return dt.fread(
            path,
            columns=['user_id', 'item_id', 'play_count']
        ).to_pandas().dropna()

    @staticmethod
    def _read_mismatches(path):
        name = 'sid_mismatches.txt'
        file = join(path, name)
        mismatches = []
        with open(file) as f:
            for line in f.readlines():
                song, track = line[
                    line.find('<') + 1: line.find('>')].split(' ')
                mismatches.append([song, track])
        return pd.DataFrame(mismatches, columns=['item_id', 'track_id'])

    @staticmethod
    def _drop_mismatches(df, mismatches):
        return df[~df.item_id.isin(mismatches)]

    @safe
    def _download(self, path):
        """
        Downloads train triplets, MSD Challenge Kaggle data
        (http://millionsongdataset.com/challenge/)
        and a list of matching errors
        http://millionsongdataset.com/blog/12-2-12-fixing-matching-errors/

        :param path: path to save
        :return: None
        """
        self.logger.info('Getting Million Song Dataset...')
        self.logger.info('Downloading Echo Nest Taste Subprofile train data...')
        base_url = 'http://millionsongdataset.com/sites/default/files/challenge/'

        download_dataset(
            base_url + 'train_triplets.txt.zip',
            join(self.data_folder, 'train.zip')
        )
        rename(join(path, 'train'), path)

        self.logger.info('Downloading evaluation data for MSD Challenge...')
        download_dataset(
            base_url + 'EvalDataYear1MSDWebsite.zip',
            join(path, 'eval.zip')
        )
        rename(
            join(path, 'EvalDataYear1MSDWebsite'),
            join(path, 'evaluation')
        )

        self.logger.info('Downloading list of matching errors...')
        url = 'http://millionsongdataset.com/sites/default/files/tasteprofile/sid_mismatches.txt'
        download_url(url, join(path, 'sid_mismatches.txt'))
