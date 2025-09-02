#!/bin/bash

# Script set us layout before start rofi, it needs for working keybindings

if ! command -v xkb-switch &> /dev/null; then
    echo "xkb-switch: command not found"
    exit 1
fi

CURRENT_LAYOUT=$(xkb-switch)

xkb-switch -s us

rofi -show "$1"

xkb-switch -s "$CURRENT_LAYOUT"
