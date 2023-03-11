#!/bin/bash

# Set initial mode, and mode names
MODE="default"
COMMAND="command"
LAYOUT="layout"

# A stub mode, used to block the script from changing workspace focus
STUB="stub"

# Set default workspace name
DEFAULT_WORKSPACE="w"

# Initialize block focus flag
BLOCK_FOCUS=0

# Function to rename workspaces
rename_workspaces() {
    # Use jq to exclude focused workspace, and workspaces with specific mode names
    local exclude=$(echo "$1" | jq --unbuffered -c "[ .[] | select(.focused or (.name|test(\"^[0-9]+:$MODE:.+\")) or (.name|test(\"^[0-9]+:$COMMAND:.+\"))) ]")
    # Sort the remaining workspaces by their numeric prefix
    local sorted=$(echo "$exclude" | jq -c 'sort_by(.name|split(":")|.[0]|tonumber)')
    # Remove mode name from workspace names
    local rename=$(echo "$sorted" | jq --unbuffered -c ".[].name |= sub(\"^[0-9]+:$MODE:\"; \"\")")
    rename=$(echo "$rename" | jq --unbuffered -c ".[].name |= sub(\"^[0-9]+:$COMMAND:\"; \"\")")
    # Return renamed workspaces
    echo "$rename"
}

# Function to switch to first workspace with current mode name, or create new one if none exist
switch_workspace() {
    # Use jq to select first workspace with current mode name, or default workspace name
    local workspace=$(echo "$1" | jq --unbuffered -r ".[] | select(.name|test(\"^[0-9]+:$MODE:.+\")).name" | head -1)
    if [[ -z $workspace ]]; then
        workspace="1:$MODE:$DEFAULT_WORKSPACE"
    fi
    # Switch to selected workspace
    i3-msg -q workspace "$workspace"
}

# Function to handle changes to mode
handle_mode_change() {
    # Check if event contains a "change" key, is not a command mode, or layout mode, and has length of 2
    if [[ $(echo "$1" | jq 'has("change")') && $(echo "$1" | jq 'length') == 2 && $(echo "$1" | jq -r '.change') != $COMMAND && $(echo "$1" | jq -r '.change') != $LAYOUT ]]; then
        # If "change" key is set to "stub", block the script from changing workspace focus
        if [[ $(echo "$1" | jq -r '.change') == $STUB ]]; then
            BLOCK_FOCUS=1
            i3-msg -q mode $MODE
        else
            # Otherwise, update mode, and switch to appropriate workspace if block focus flag is not set
            MODE=$(echo "$1" | jq -r '.change')
            if [[ $BLOCK_FOCUS == 0 ]]; then
                switch_workspace "$2"
            fi
            BLOCK_FOCUS=0
        fi
    fi
}

# Get initial workspace information
i3-msg -t get_workspaces

# Subscribe to events and listen for changes
i3-msg -t subscribe -m '["workspace", "output", "mode"]' | {
    while read x ; do
        workspaces=$(i3-msg -t get_workspaces)
        handle_mode_change "$x" "$workspaces"
        renamed=$(rename_workspaces "$workspaces")
        echo "$renamed"
    done
}
