#!/usr/bin/env python3

from i3ipc import Connection
import wmfocus
import stash

if __name__ == "__main__":

    i3 = Connection()

    tree = i3.get_tree()
    workspace = tree.find_focused().workspace().name

    if stash.is_minor(workspace):
        i3.command("workspace %s" % stash.major(workspace))
    else:
        minor = stash.minor(workspace)
        i3.command("workspace %s" % minor)

        windows = 0;
        for con in tree:
            if (con.window and con.parent.type != 'dockarea' and con.workspace().name == minor):
                windows += 1

        if windows > 1:
            i3.command('[id="%s"] focus' % wmfocus.choose_window())
