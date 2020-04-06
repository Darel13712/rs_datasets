from urllib.request import urlretrieve

from tqdm import tqdm

from rs_datasets.data_loader.archives import extract, rm_if_exists


def download_dataset(
        url: str, destination_path: str, manage_folder: bool = True):
    """
    Download dataset from the internet.

    :param url: from where
    :param destination_path: where to
    :param manage_folder: check if there is root folder in archive:
        if there is one, do not create extra folder,
        if there are just files inside, put them into folder.
        If param is set to `False`, extract "as is".
    :return: None
    """
    download_url(url, destination_path)
    extract(destination_path, manage_folder)
    rm_if_exists(destination_path)


def download_url(url: str, filename: str):
    """
    Download something from link.

    :param url: link
    :param filename: path to save
    :return: None
    """
    with tqdm(unit='B', unit_scale=True) as progress:
        def report(chunk, chunksize, total):
            progress.total = total
            progress.update(chunksize)
        return urlretrieve(url, filename, reporthook=report)
