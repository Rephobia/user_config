#!/usr/bin/env python3

import os
import glob
from datetime import datetime

def build():
    _create_links(_builder_directory('home'), _home_directory())
    _create_links(_builder_directory('.config'), _home_directory('.config'))

def unbuild():
    _undo_links(_builder_directory('home'), _home_directory())
    _undo_links(_builder_directory('.config'), _home_directory('.config'))

def _builder_directory(subdirectory: str = '') -> str:
    """
    returns path to builder directory, has optional subdirectory path parameter, that concat to result
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), subdirectory)

def _home_directory(subdirectory: str = '') -> str:
    """
    returns path to home directory, has optional subdirectory path parameter, that concat to result
    """
    return os.path.join(os.getenv('HOME'), subdirectory)


def _create_links(src_path: str, dst_path: str) -> None:
    """
    creates links to all files from src_path to dst_path, also creates backup
    by mask 'original_file_name.bak.timestamp'
    """

    file_names = _get_file_names(src_path)

    src_paths = map(lambda x: os.path.join(src_path, x), file_names)
    dst_paths = map(lambda x: os.path.join(dst_path, x), file_names)

    for src_path, dst_path in dict(zip(src_paths, dst_paths)).items():
        _symlink(src_path, dst_path)

def _undo_links(src_path: str, dst_path: str) -> None:
    """
    removes links to all files from src_path to dst_path, if link in dst_path has backup
    by mask 'original_file_name.bak.timestamp'
    """
    file_names = _get_file_names(src_path)

    for original_file_name in file_names:
        backups = filter(lambda x: _is_backup(original_file_name, x), os.listdir(dst_path))
        backups = sorted(backups, reverse=True, key=_get_datetime)
        backup = next(iter(backups), None)
        if (backup):
            os.replace(os.path.join(dst_path, backup), os.path.join(dst_path, original_file_name))

def _get_file_names(path: str) -> list:
    """
    tries to get directory file names list, if directory doesn't exists raise Exception
    """
    if not os.path.exists(path):
        raise Exception('Try to get directory files, but directory: ' + path + ' does not exists')

    return os.listdir(path)

def _symlink(src_path: str, dst_path: str) -> None:
    """
    is os.symlink wrapper, which creates backup for old dst_path symlink/file if it exists
    """
    if os.path.exists(dst_path) or os.path.islink(dst_path):
        os.replace(dst_path, dst_path + '.bak.' + datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
    os.symlink(src_path, dst_path)


def _is_backup(original_file_name: str, file_name: str) -> bool:
    """
    checks if file_name has mask 'original_file_name.bak.timestamp'
    """
    if not file_name.startswith(original_file_name + '.bak'):
        return False

    try:
        _get_datetime(file_name)
        return True
    except ValueError:
        return False

def _get_datetime(file_name: str) -> str:
    """
    splits file_name by dots and get last segment as datetime or throws ValueError
    """
    return datetime.strptime(file_name.split('.')[-1], '%Y-%m-%d-%H:%M:%S')
