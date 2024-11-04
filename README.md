# Dependencies

- Python3 - ansible dependency
- Just - command runner, install from rust cargo or build from source https://github.com/casey/just 

# Justfile recipes

```shell
default                          # list of all justfile recipes
venv                             # create python virtual environment for ansible
vault-file command path          # manipulate vault files
playbook playbook                # run playbook by name
playbook-with-tags playbook tags # run playbook by name with tags
localhost-st                     # configure st
localhost-cli                    # configure cli (.bashrc, .inputrc)
localhost-i3-desktop             # configure i3wm with desktop i3bar
localhost-i3-laptop              # configure i3wm with laptop i3bar
localhost-gpg                    # configure gpg
localhost-dmenu                  # configure dmenu
localhost-syncthing              # configure syncthing
localhost-samba                  # configure samba
localhost-all                    # run all localhost playbooks
nas-qbittorrent                  # configure qbittorrent on nas
nas-samba                        # configure samba on nas
nas-syncthing                    # configure syncthing on nas
nas-all                          # run all nas playbooks
```
