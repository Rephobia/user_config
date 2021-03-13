#!/usr/bin/env python3

from i3ipc import Connection
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
    
def focus_window(winid : int):
    i3.command('[id="%d"] focus' % winid)
    
def restore_workspaces(memorycons: List[MemoryCon]):
    for window in memorycons:
        window.move_to_workspace(window.last_workspace);
