#!/usr/bin/env python3

"""
Module wrapper for i3ipc workspaces
"""
from i3ipc import Connection

class Workspace:
    i3 = Connection()

    @staticmethod
    def get_all_names(is_exclude_focused: bool = True) -> list:
        """
        Get all workspaces, remove focused workspace if is_exclude_focused
        flag passed
        """
        i3_tree = Workspace.i3.get_tree()
        ws_current = i3_tree.find_focused().workspace()
        if (is_exclude_focused):
            return [ws.name for ws in i3_tree.workspaces() if ws.id != ws_current.id]

        return [ws.name for ws in i3_tree.workspaces()]
