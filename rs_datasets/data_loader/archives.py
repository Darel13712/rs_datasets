import os
import tarfile
from os.path import splitext
from tarfile import TarFile
from typing import Union
from zipfile import ZipFile


def extract(archive_name: str, manage_folder: bool = True) -> None:
    """
    Extract `archive_name` and put it inside a folder
    if there are multiple files inside.

    :param archive_name: path to archive
    :param manage_folder: check if there is root folder in archive:
        if there is one, do not create extra folder,
        if there are just files inside, put them into folder.
        If param is set to `False`, extract "as is".
    :return:
    """
    if archive_name.endswith('.zip'):
        archive = ZipFile(archive_name)
    else:
        try:
            archive = tarfile.open(archive_name)
        except Exception:
            raise NotImplementedError(f'Can\'t extract {archive_name}')

    name = os.path.dirname(archive_name)
    if manage_folder and not contains_dir(archive):
        name = remove_extension(archive_name)
        os.mkdir(name)

    archive.extractall(path=name)
    archive.close()


def rm_if_exists(filepath: str) -> None:
    """
    Remove file if it exists, else do nothing.

    :param filepath: path to file
    :return: None
    """
    if os.path.exists(filepath):
        os.remove(filepath)


def contains_dir(archive: Union[ZipFile, TarFile]) -> bool:
    """
    Check if archive contains a root folder or just files.

    :param archive: archive file
    :return: `True` if first element of archive is folder
    """
    if isinstance(archive, ZipFile):
        contents = archive.infolist()
        is_dir = contents[0].is_dir()
    elif isinstance(archive, TarFile):
        contents = archive.getmembers()
        is_dir = contents[0].isdir()
    else:
        raise TypeError(f'Unknown archive type: {type(archive)}')
    return is_dir


def remove_extension(file: str) -> str:
    """
    Get file name without _last_ extension.

    :param file: string
    :return: archive.tar.gz -> archive.tar
    """
    return splitext(file)[0]
