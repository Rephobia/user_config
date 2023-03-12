#!/bin/bash
i3-msg -t get_workspaces | jq -r '.[].name' | dmenu | {
    read workspace;
    if [[ $workspace ]]; then
	i3-msg move container to workspace $workspace
    fi
}
