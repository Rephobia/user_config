#!/usr/bin/env python3

import os
import importlib.util
import sys

def get_builders():
    """
    collects python files in builders subdirectories and tries to load them as module,
    this function returns generator
    """
    directory = os.path.dirname(os.path.abspath(__file__))
    for entity_name in os.listdir(directory):
        entity_path = os.path.join(directory, entity_name, '__init__.py');
        if os.path.exists(entity_path):
            yield _load_module(entity_name, entity_path)

def _load_module(file_name: str, file_path: str):
    """
    tries to load module from passed file_name and file_path
    """
    spec = importlib.util.spec_from_file_location(file_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[file_name] = module
    spec.loader.exec_module(module)

    return module
