from i3ipc import Con, Connection, Event

class Window(Con):

    def __init__(self, data, parent, conn):
        Con.__init__(self, data, parent, conn)
        self._save_last_workspace()


    def move_to_workspace(self, workspace: str):
        self._save_last_workspace()
        super().command("move container to workspace %s" % workspace);
        
    def _save_last_workspace(self):
        self.last_workspace = super().workspace().name
