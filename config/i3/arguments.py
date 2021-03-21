#!/usr/bin/env python3

import argparse

class _Arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--wm_class', nargs='+', type=str, help="select windows by wm_class")
    
    args = parser.parse_args()

def wm_class() -> list:

    return _Arguments.args.wm_class
