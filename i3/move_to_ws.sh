#!/bin/bash

gen_workspaces=$(i3-msg -t get_workspaces | tr ',' '\n' | grep "name" | sed 's/"name":"\(.*\)"/\1/g' | sort -n)

selected_workspace=$(echo -e "$gen_workspaces" | rofi -dmenu -p 'move to ws')

i3-msg move container to workspace "$selected_workspace"
