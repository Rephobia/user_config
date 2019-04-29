#!/bin/bash

gen_wkspaces=$(i3-msg -t get_wkspaces | tr ',' '\n' | grep "name" | sed 's/"name":"\(.*\)"/\1/g' | st -n)

selected_wkspace=$(echo -e "$gen_wkspaces" | rofi -dmenu -p 'move to ws')

i3-msg move container to wkspace "$selected_wkspace"
