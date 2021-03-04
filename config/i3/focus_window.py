#!/usr/bin/env python3

from i3ipc import Con, Connection, Event
import os
import subprocess

class Window(Con):

    def __init__(self, data, parent, conn):
        Con.__init__(self, data, parent, conn)
        self._save_last_workspace()


    def move_to_workspace(self, workspace):
        self._save_last_workspace()
        super().command("move container to workspace %s" % workspace);
        
    def _save_last_workspace(self):
        self.last_workspace = super().workspace().name
        
class Manager:
    
    i3 = Connection()

    def move_all_windows(workspace):
        windows = []
        for con in Manager.i3.get_tree():
            if con.window and con.parent.type != 'dockarea' and con.workspace().name != '__i3_scratch':
                window = Window(con.ipc_data, con.parent, con._conn)
                window.move_to_workspace(workspace)
                windows.append(window)
        return windows
    
    def focus_workspace(workspace):
        Manager.i3.command("workspace %s" % workspace)

    def focus_window(container):
        Manager.i3.command('[id="%d"] focus' % container.window)

    def choose_window():
        subprocess.call([os.path.expanduser('~/.config/i3/winswitch/winswitch')])
        return Manager.i3.get_tree().find_focused()

    def restore_workspaces(windows):
        for container in windows:
            container.move_to_workspace(container.last_workspace);



windows = Manager.move_all_windows("tmp")

Manager.focus_workspace("tmp")

focused_window = Manager.choose_window()

Manager.restore_workspaces(windows);

Manager.focus_window(focused_window)

