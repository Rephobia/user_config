#!/bin/bash

repo="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"

repo_config_dir=$repo/config
repo_home_dir=$repo/home


local_home_dir="$HOME/"
local_config_dir="$HOME/.config/"


shopt -s dotglob # enable hidden files


if [ "$1" == "delete" ];
then
    for file in $repo_config_dir/*; do
	rm -i $local_config_dir$(basename $file)
    done

    for file in $repo_home_dir/*; do
	rm -i $local_home_dir$(basename $file)
    done
else
    ln -sfn $repo_config_dir/* $local_config_dir
    ln -sfn $repo_home_dir/* $local_home_dir
fi
