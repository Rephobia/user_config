#!/usr/bin/env python3

import manager
import winswitch

if __name__ == "__main__":
    
    memorycons = manager.move_windows("tmp")

    manager.focus_workspace("tmp")

    winid = winswitch.choose_window()
    
    manager.restore_workspaces(memorycons);
    
    manager.focus_window(winid)

