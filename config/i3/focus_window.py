#!/usr/bin/env python3

from i3ipc import Connection, Event
import subprocess

i3 = Connection()

focused = i3.get_tree()

windows = []

for con in i3.get_tree():
    if con.window and con.parent.type != 'dockarea' and con.workspace().name != '__i3_scratch':
        con.last_workspace = con.workspace().name
        con.command("move container to workspace tmp");
        windows.append(con);

i3.command("workspace tmp")

subprocess.call(["/home/foobar/.config/i3/winswitch/winswitch"])

focused = i3.get_tree().find_focused()

for con in windows:
    con.command("move container to workspace %s" % con.last_workspace);

i3.command('[id="%d"] focus' % focused.window)
