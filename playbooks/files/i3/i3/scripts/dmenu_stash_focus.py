#!/usr/bin/env python3

"""
Get stash workspaces exclude current and pass they in dmenu. 
Chosen workspace will be focused.
If stash have only two workspaces toggle switch between them, without dmenu
If stash empty, focus prefix workspace.
"""

from i3ipc import Connection
from lib.stash import Stash
from lib.dmenu import Dmenu

if __name__ == "__main__":

    workspaces = Stash.get_workspaces()
    if (workspaces):
        if (len(workspaces) > 1):
            choosen = Dmenu.show_values([ws.name for ws in workspaces])
            if (choosen):
                Connection().command("workspace %s" % choosen)
        else:
            Connection().command("workspace %s" % workspaces[0].name)
    else:
        ws_current = Connection().get_tree().find_focused().workspace().name
        Connection().command("workspace %s" % Stash.get_workspace_prefix(ws_current))
