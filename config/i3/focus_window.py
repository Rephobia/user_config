#!/usr/bin/env python3

import manager

if __name__ == "__main__":
    windows = manager.move_all_windows("tmp")

    manager.focus_workspace("tmp")

    focused_window = manager.choose_window()

    manager.restore_workspaces(windows);

    manager.focus_window(focused_window)

