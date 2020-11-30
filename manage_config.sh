#!/bin/bash

user_config_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )/"
home_dir="$HOME/"
config_dir="$HOME/.config/"

declare -a home_files=(".bashrc"
		       ".inputrc")
declare -a config_files=("lxterminal/lxterminal.conf"
			 "i3/config"
			 "i3/dmenu_starter.sh"
			 "i3/gen_workspaces.sh"
			 "i3/move_to_ws.sh"
			 "i3status/config"
			 "rofi/config")

function symlink_dst_src() {
    local dst=$1
    shift
    local src=("$@")

    for i in "${src[@]}"
    do
     	mkdir -p $(dirname "$dst$i") && ln -sfn "$user_config_dir$i" "$dst$i"
    done
}

function remlink_dst_src() {
    local dst=$1
    shift
    local src=("$@")

    for i in "${src[@]}"
    do
     	rm -i "$dst$i"
    done
}


if [ "$1" == "delete" ];
then
    remlink_dst_src "$home_dir" "${home_files[@]}"
    remlink_dst_src "$config_dir" "${config_files[@]}"
else
    symlink_dst_src "$home_dir" "${home_files[@]}"
    symlink_dst_src "$config_dir" "${config_files[@]}"
fi
