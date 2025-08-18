#!/bin/bash

playerctl --follow status | while read state; do
    if [ "$state" = "Playing" ]; then
        xset -dpms s off
        xset s off
    else
        xset +dpms s on
        xset s on
    fi
done
