#!/usr/bin/env python3

import os
import subprocess

def choose_window() -> int:
    winid = subprocess.check_output([os.path.expanduser('~/.config/i3/winswitch/winswitch')])
    return int(winid.decode("utf-8"))
