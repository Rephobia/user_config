#!/usr/bin/env python3

import os
import subprocess

from i3ipc import Con, Connection
from typing import List

from memorycon import MemoryCon

        
i3 = Connection()

def move_windows(workspace: str) -> List[MemoryCon]:
    memorycons = []
    for con in i3.get_tree():
        if con.window and con.parent.type != 'dockarea' and con.workspace().name != '__i3_scratch':
            memorycon = MemoryCon(con)
            memorycon.move_to_workspace(workspace)
            memorycons.append(memorycon)
    return memorycons
    
def focus_workspace(workspace: str):
    i3.command("workspace %s" % workspace)
    
def focus_window(con: MemoryCon):
    i3.command('[id="%d"] focus' % con.window)

def choose_window() -> Con:
    subprocess.call([os.path.expanduser('~/.config/i3/winswitch/winswitch')])
    return i3.get_tree().find_focused()

def restore_workspaces(memorycons: List[MemoryCon]):
    for window in memorycons:
        window.move_to_workspace(window.last_workspace);
