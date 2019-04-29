#!/bin/bash

i3-msg -t get_wkspaces | tr ',' '\n' | grep "name" | sed 's/"name":"\(.*\)"/\1/g' | st -n
