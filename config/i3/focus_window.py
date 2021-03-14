#!/usr/bin/env python3

import i3
import wmfocus

if __name__ == "__main__":
    
    memorycons = i3.move_windows("tmp")

    i3.focus_workspace("tmp")

    i3.set_layout(memorycons, rowsize = 3)
    
    winid = wmfocus.choose_window()
    
    i3.restore_workspaces(memorycons)
    
    i3.focus_window(winid)

