#!/usr/bin/env python3

import argparse
import sys

import builders

class ConsoleColors:
    ERROR = '\033[0;31m'
    ENDC = '\033[0m'

parser = argparse.ArgumentParser()
parser.add_argument('mode', type=str, help='What commands to use, (build, unbuild)')
args = parser.parse_args()

modes = {
    'build': lambda x: x.build(),
    'unbuild': lambda x: x.unbuild()
}

mode = modes.get(args.mode, None)

if not mode:
    print(ConsoleColors.ERROR + '\nWrong command line argument\n' + ConsoleColors.ENDC)
    parser.print_help()
    sys.exit()

for builder in builders.get_builders():
    try:
        modes[args.mode](builder)
    except Exception as error:
        print(ConsoleColors.ERROR + 'Error: ' + ConsoleColors.ENDC, error)
