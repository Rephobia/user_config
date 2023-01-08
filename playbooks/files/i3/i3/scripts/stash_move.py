#!/usr/bin/env python3

"""
Get prefix from workspace and move focused container in prefix workspace.
It works with i3wsr, that adds app name to workspace, eg:
1) we have focused container 'Emacs' in workspace '1 Emacs | Firefox', where '1' is prefix
2) after move Emacs in '1' workspace, i3wsr renames workspace '1' to '1 Emacs'

But it doesn't work correctly with duplicate names, if we already have workspace '1 Emacs',
new workspace will be '1'
"""

from i3ipc import Connection
from lib.stash import Stash

if __name__ == "__main__":

    i3 = Connection()
    prefix = Stash.get_workspace_prefix(i3.get_tree().find_focused().workspace().name)
    i3.command("move container to workspace %s" % prefix)
