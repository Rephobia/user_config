#!/bin/bash

repo="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null 2>&1 && pwd )"

repo_config_dir=$repo/config
repo_home_dir=$repo/home


local_home_dir="$HOME/"
local_config_dir="$HOME/.config/"

build_st()
{
    git init $repo/st/
    git -C $repo/st/ remote add -f origin https://git.suckless.org/st
    git -C $repo/st/ checkout master
    git -C $repo/st/ apply $repo/st/*.diff
    
    make -C $repo/st/
    sudo make -C $repo/st/ install
}

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
    build_st
fi
