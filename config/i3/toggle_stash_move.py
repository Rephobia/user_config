#!/usr/bin/env python3

from i3ipc import Connection
import stash

if __name__ == "__main__":

    i3 = Connection()

    workspace = i3.get_tree().find_focused().workspace().name

    if stash.is_minor(workspace):
        i3.command("move container to workspace %s" % stash.major(workspace));
    else:
        i3.command("move container to workspace %s" % stash.minor(workspace));
