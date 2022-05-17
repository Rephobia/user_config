#!/usr/bin/env python3

import argparse
import sys
import builders

from types import ModuleType
from typing import Callable

class ConsoleColors:
    ERROR = '\033[0;31m'
    END_COLOR = '\033[0m'
    OK = '\u001b[38;5;70m'

    
def build(builder: ModuleType) -> None:
    """
    is builder wrapper, that adds colored output
    """
    print(f'{ConsoleColors.OK}\nStart \'{builder.__name__}\' builder{ConsoleColors.END_COLOR}')
    builder.build()
    print(f'{ConsoleColors.OK}Finish \'{builder.__name__}\' builder\n{ConsoleColors.END_COLOR}')

def unbuild(builder: ModuleType) -> None:
    """
    is unbuilder wrapper, that adds colored output
    """
    print(f'{ConsoleColors.OK}\nStart \'{builder.__name__}\' unbuilder{ConsoleColors.END_COLOR}')
    builder.unbuild()
    print(f'{ConsoleColors.OK}Finish \'{builder.__name__}\' unbuilder\n{ConsoleColors.END_COLOR}')

def get_current_mode(user_passed_mode: str) -> Callable:
    """
    tries to get builder mode (build, unbuild) from user input,
    if passed mode doesn't exist print error and exit
    """
    modes = {
        'build': build,
        'unbuild': unbuild
    }

    mode = modes.get(user_passed_mode, None)

    if not mode:
        print(f'{ConsoleColors.ERROR} \nError: Wrong command line argument\n {ConsoleColors.END_COLOR}')
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
            print(f'{ConsoleColors.ERROR}Error: {ConsoleColors.END_COLOR}', error)
