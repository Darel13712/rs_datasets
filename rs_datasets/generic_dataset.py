import logging
import os
import shutil
from os.path import join

from pandas import DataFrame, Series
from datatable import Frame


class Dataset:
    def __init__(self, path: str = None):
        data_folder = (path or os.getenv('RS_DATASETS', None) or
                       self.default_folder)
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        self.data_folder = data_folder
        logger = logging.getLogger("rs_datasets")
        logger.setLevel(logging.INFO)
        self.logger = logger
        try:
            display = __import__('IPython.core.display', globals(), locals(), ['display'])
            self.display = display.display
        except Exception:
            self.display = print

    @property
    def default_folder(self):
        root = os.path.expanduser('~')
        return join(root, 'rs_datasets')

    def info(self):
        for name, df in self.__dict__.items():
            if isinstance(df, Frame) or isinstance(df, DataFrame) or isinstance(df, Series):
                print(name)
                self.display(df.head(3))
                print()


def safe(func):
    def decorated(self, path, *args, **kwargs):
        try:
            func(self, path, *args, **kwargs)
        except Exception as e:
            if os.path.exists(path):
                shutil.rmtree(path)
            raise e
    return decorated
