# Dependencies

- Python3 - ansible dependency
- Just - command runner, install from rust cargo or build from source https://github.com/casey/just 

# Justfile recipes

```shell
default         # list of all justfile recipes
venv            # create python virtual environment for ansible
local-st        # configure st
local-cli       # configure cli (.bashrc, .inputrc)
local-i3        # configure i3wm
local-all       # run all local playbooks
nas-qbittorrent # configure qbittorrent on nas
nas-samba       # configure samba on nas
nas-all         # run all nas playbooks
```
