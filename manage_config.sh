#!/bin/bash

user_config_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"
sys_config_dir="$HOME/.config"

bashrc=".bashrc"
inputrc=".inputrc"

declare -a dot_config_files=("lxterminal/config"
			     "i3/config"
			     "i3/dmenu_starter.sh"
			     "i3/gen_wkspaces.sh"
			     "i3/move_to_ws.sh"
			     "i3status/config"
			     "rofi/config")

if [ "$1" == "delete" ];
then
    rm -i ~/.bashrc ~/.inputrc

    f i in "${dot_config_files[@]}"
    do
	rm -i "$sys_config_dir/$i"
    done
else
    ln -sfn  "$user_config_dir/$bashrc" ~/.bashrc
    ln -sfn  "$user_config_dir/$inputrc" ~/.inputrc

    f i in "${dot_config_files[@]}"
    do
	ln -sfn "$user_config_dir/$i" "$sys_config_dir/$i"
    done
fi
