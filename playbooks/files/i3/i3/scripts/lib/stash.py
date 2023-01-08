#!/usr/bin/env python3

"""
Stash is a collection of another workspaces with equal prefixes, eg:
1 Emacs | st
1 Firefox
1 Anki
2 Telegram
2 Thunderbird
We have five workspaces and two stashes
"""

from i3ipc import Connection

class Stash:
    i3 = Connection()
    SEPARATOR = " "

    @staticmethod
    def get_workspace_prefix(ws_name: str) -> str:
        """
        Extract stash prefix by separator
        """
        end = ws_name.find(Stash.SEPARATOR)
        return ws_name[0:end] if end > 0 else ws_name

    @staticmethod
    def get_workspaces(is_exclude_focused: bool = True) -> list:
        """
        Get stashed workspaces, remove focused workspace if is_exclude_focused
        flag passed
        """
        ws_current = Stash.i3.get_tree().find_focused().workspace()
        ws_current_prefix = Stash.get_workspace_prefix(ws_current.name)
        result = [];
        for ws in Stash.i3.get_tree().workspaces():
            if (ws.name and ws_current_prefix == Stash.get_workspace_prefix(ws.name)):
                if (is_exclude_focused and ws.id == ws_current.id) :
                    continue
                else:
                    result.append(ws)
        return result

    @staticmethod
    def get_containers(is_exclude_focused: bool = True) -> list:
        """
        Get stashed containers, remove focused container if is_exclude_focused
        flag passed
        """
        current_container = Stash.i3.get_tree().find_focused()
        current_prefix = Stash.get_workspace_prefix(current_container.workspace().name)
        result = [];
        for ws in Stash.i3.get_tree().workspaces():
            if (ws.name and current_prefix == Stash.get_workspace_prefix(ws.name)):
                if (is_exclude_focused) :
                    for container in ws.leaves() + ws.floating_nodes:
                        if (container.id != current_container.id):
                            result.append(container)
                else:
                    result += ws.leaves() + ws.floating_nodes
        return result
