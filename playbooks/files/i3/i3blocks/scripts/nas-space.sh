#!/bin/bash

BASE="/run/user/$(id -u)/gvfs"

DIR=$(find "$BASE" -maxdepth 1 -type d -name "smb-share:*" 2>/dev/null | head -n1)

if [ -z "$DIR" ]; then
    echo "NAS: OFF"
    exit 0 
fi

DATA=$(timeout 2 df -h "$DIR" 2>/dev/null | awk '{print $4}' | tail -1)

if [ -z "$DATA" ]; then
    echo "NAS: ?"
    exit 0
fi


echo $DATA
