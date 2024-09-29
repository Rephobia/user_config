# Dependencies

- Python3 - ansible dependency
- Just - command runner, install from rust cargo or build from source https://github.com/casey/just 

# Justfile recipes

```shell
default                 # list of all justfile recipes
venv                    # create python virtual environment for ansible
vault-file command path # manipulate vault files
playbook playbook       # run playbook by name
localhost-st            # configure st
localhost-cli           # configure cli (.bashrc, .inputrc)
localhost-i3            # configure i3wm
localhost-gpg           # configure gpg
localhost-dmenu         # configure dmenu
localhost-samba         # configure samba
localhost-syncthing     # configure syncthing
localhost-all           # run all localhost playbooks
nas-qbittorrent         # configure qbittorrent on nas
nas-samba               # configure samba on nas
nas-syncthing           # configure syncthing on nas
nas-all                 # run all nas playbooks
```
