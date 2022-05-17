#!/usr/bin/env python3

import argparse
import sys
import builders

from types import ModuleType
from typing import Callable

class ConsoleColors:
    ERROR = '\033[0;31m'
    ENDC = '\033[0m'

def get_current_mode(user_passed_mode: str) -> Callable:
    modes = {
        'build': lambda x: x.build(),
        'unbuild': lambda x: x.unbuild()
    }

    mode = modes.get(user_passed_mode, None)

    if not mode:
        print(ConsoleColors.ERROR + '\nWrong command line argument\n' + ConsoleColors.ENDC)
        parser.print_help()
        sys.exit()

    return mode


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, help='What commands to use, (build, unbuild)')
    args = parser.parse_args()

    mode = get_current_mode(args.mode)

    for builder in builders.get_builders():
        try:
            mode(builder)
        except Exception as error:
            print(ConsoleColors.ERROR + 'Error: ' + ConsoleColors.ENDC, error)
