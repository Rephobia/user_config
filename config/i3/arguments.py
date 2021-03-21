#!/usr/bin/env python3

import argparse

_PARSER = argparse.ArgumentParser()
_PARSER.add_argument('--wm_class', nargs='+', type=str, help="select windows by wm_class")
    
_ARGS = _PARSER.parse_args()

def wm_class() -> list:

    return _ARGS.wm_class if _ARGS.wm_class else []
