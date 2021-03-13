from i3ipc import Con

class MemoryCon(Con):

    def __init__(self, con: Con):
        Con.__init__(self, con.ipc_data, con.parent, con._conn)
        self._save_last_workspace()

    def move_to_workspace(self, workspace: str):
        self._save_last_workspace()
        super().command("move container to workspace %s" % workspace);
        
    def _save_last_workspace(self):
        self.last_workspace = super().workspace().name
