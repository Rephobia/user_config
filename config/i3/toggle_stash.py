#!/usr/bin/env python3

from i3ipc import Connection
import wmfocus

def remove_prefix(prefix, text):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


if __name__ == "__main__":

    i3 = Connection()

    stash_prefix = "s:"
    workspace_name = i3.get_tree().find_focused().workspace().name
    if workspace_name.startswith(stash_prefix):
        i3.command("workspace %s" % remove_prefix(stash_prefix, workspace_name))
    else:
        i3.command("workspace %s" % stash_prefix + remove_prefix(stash_prefix, workspace_name))
        windows = 0;
        for con in i3.get_tree():
            if (con.window and con.parent.type != 'dockarea' and con.workspace().name == stash_prefix + remove_prefix(stash_prefix, workspace_name)):
                windows += 1
        if windows > 1:
            i3.command('[id="%s"] focus' % wmfocus.choose_window())
