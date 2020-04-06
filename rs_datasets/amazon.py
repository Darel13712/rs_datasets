from os import mkdir
from os.path import join, exists

import datatable as dt

from rs_datasets.data_loader import download_url
from rs_datasets.generic_dataset import Dataset, safe

categories = {
    'fashion': 'AMAZON_FASHION.csv',
    'beauty': 'All_Beauty.csv',
    'appliances': 'Appliances.csv',
    'arts': 'Arts_Crafts_and_Sewing.csv',
    'automotive': 'Automotive.csv',
    'books': 'Books.csv',
    'cds': 'CDs_and_Vinyl.csv',
    'phones': 'Cell_Phones_and_Accessories.csv',
    'clothing': 'Clothing_Shoes_and_Jewelry.csv',
    'music': 'Digital_Music.csv',
    'electronics': 'Electronics.csv',
    'cards': 'Gift_Cards.csv',
    'grocery': 'Grocery_and_Gourmet_Food.csv',
    'kitchen': 'Home_and_Kitchen.csv',
    'scientific': 'Industrial_and_Scientific.csv',
    'kindle': 'Kindle_Store.csv',
    'luxury': 'Luxury_Beauty.csv',
    'subscriptions': 'Magazine_Subscriptions.csv',
    'movies': 'Movies_and_TV.csv',
    'musical instruments': 'Musical_Instruments.csv',
    'office': 'Office_Products.csv',
    'garden': 'Patio_Lawn_and_Garden.csv',
    'pet': 'Pet_Supplies.csv',
    'pantry': 'Prime_Pantry.csv',
    'software': 'Software.csv',
    'sports': 'Sports_and_Outdoors.csv',
    'tools': 'Tools_and_Home_Improvement.csv',
    'toys': 'Toys_and_Games.csv',
    'games': 'Video_Games.csv'
}


class Amazon(Dataset):
    def __init__(self, category, path: str = None):
        """
        :param category: one of {'fashion', 'beauty', 'appliances', 'arts', 'automotive',
              'books', 'cds', 'phones', 'clothing', 'music', 'electronics',
              'cards', 'grocery', 'kitchen', 'scientific', 'kindle', 'luxury',
              'subscriptions', 'movies', 'musical instruments', 'office', 'garden',
              'pet', 'pantry', 'software', 'sports', 'tools', 'toys', 'games}
        :param path: folder which is used to download dataset to
            if it does not contain dataset files.
            If files are found, load them.
        """
        super().__init__(path)
        if category not in categories:
            raise ValueError(f'Dataset category must be one of {categories.keys()}')
        folder = join(self.data_folder, 'amazon')
        if not exists(folder):
            mkdir(folder)
        if not exists(join(folder, category + '.csv')):
            self._download(folder, category)
        self.ratings = dt.fread(
            join(folder, category + '.csv'),
            columns=['user_id', 'item_id', 'rating']
        ).to_pandas()


    @safe
    def _download(self, path, category):
        self.logger.info(f'Downloading Amazon {category} ratings...')
        base_url = 'http://deepyeti.ucsd.edu/jianmo/amazon/categoryFilesSmall/'
        url = base_url + categories[category]
        download_url(url, join(path, category + '.csv'))
