#!/usr/bin/env python3

from i3ipc import Con, Connection, Event
from typing import List

from window import Window
import os
import subprocess
        
i3 = Connection()

def move_all_windows(workspace: str) -> List[Window]:
    windows = []
    for con in i3.get_tree():
        if con.window and con.parent.type != 'dockarea' and con.workspace().name != '__i3_scratch':
            window = Window(con.ipc_data, con.parent, con._conn)
            window.move_to_workspace(workspace)
            windows.append(window)
    return windows
    
def focus_workspace(workspace: str):
    i3.command("workspace %s" % workspace)
    
def focus_window(window: Window):
    i3.command('[id="%d"] focus' % window.window)

def choose_window() -> Con:
    subprocess.call([os.path.expanduser('~/.config/i3/winswitch/winswitch')])
    return i3.get_tree().find_focused()

def restore_workspaces(windows: List[Window]):
    for window in windows:
        window.move_to_workspace(window.last_workspace);

