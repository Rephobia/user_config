#!/usr/bin/env python3

"""
Get all workspaces exclude current and pass they in dmenu.
Focused container will move to chosen workspace
"""

from i3ipc import Connection
from lib.dmenu import Dmenu
from lib.workspace import Workspace

if __name__ == "__main__":

    choosen = Dmenu.show_values(Workspace.get_all_names())
    if (choosen):
        Connection().command("move container to workspace %s" % choosen)
