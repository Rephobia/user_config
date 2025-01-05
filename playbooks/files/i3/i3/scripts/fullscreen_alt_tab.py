#!/bin/python3

from i3ipc import Connection, Con


if __name__ == "__main__":

    i3 = Connection()

    focused = i3.get_tree().find_focused()
    if (focused.fullscreen_mode) :
        i3.command("fullscreen disable; focus right; fullscreen enable")
    else:
        i3.command("focus right")
