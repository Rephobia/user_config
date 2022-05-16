#!/usr/bin/env python3

import os
import subprocess
import shutil
from git import Repo

def build():
    builder_directory = os.path.dirname(os.path.abspath(__file__))
    st_directory = os.path.join(builder_directory, 'st')

    repository = _init_repository(st_directory)
    _copy_files(os.path.join(builder_directory, 'copy_files'), st_directory)
    _apply_patches(repository, os.path.join(builder_directory, 'patches'))
    _make(st_directory)
    _clean(repository)

def unbuild():
    pass

def _init_repository(directory: str) -> Repo:
    """
    initializes repository object by directory, 
    be careful, this function also calls 'git clean -f' and 'git checkout'
    """
    repository = Repo(directory)
    repository.git.config('--global', '--add', 'safe.directory', directory)
    _clean(repository)
    return repository

def _copy_files(src: str, dst:str) -> None:
    """
    copies all files from src to dst
    """
    file_names = os.listdir(src)
    for file_name in file_names:
        shutil.copyfile(os.path.join(src, file_name), os.path.join(dst, file_name))

def _apply_patches(repository: Repo, patches_directory: str) -> None:
    """
    applies all patches from patches_directory to repository object
    """
    file_names = os.listdir(patches_directory)
    for file_name in file_names:
        repository.git.apply(os.path.join(patches_directory, file_name))

def _make(directory: str) -> None:
    """
    calls 'make' and 'make clean install' commands in passed directory
    """
    subprocess.call(['make'], cwd=directory)
    subprocess.call(['make', 'clean','install'], cwd=directory)

def _clean (repository: Repo) -> None:
    """
    cleans the repository changes and new files
    """
    repository.git.checkout('.')
    repository.git.clean('-f')
