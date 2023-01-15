# list of all justfile recipes
default:
    just --list --unsorted

# create python virtual environment for ansible
venv:
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

# manipulate vault files
vault-file command path:
    ./venv/bin/ansible-vault {{command}} {{path}} --vault-password-file .ansible_vault

# run playbook by name
playbook playbook: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/{{playbook}}.yaml --vault-password-file .ansible_vault

# configure st
localhost-st:
    just playbook localhost-st

# configure cli (.bashrc, .inputrc)
localhost-cli:
    just playbook localhost-cli

# configure i3wm
localhost-i3:
    just playbook localhost-i3

# configure gpg
localhost-gpg:
    just playbook localhost-gpg

# configure dmenu
localhost-dmenu:
    just playbook localhost-dmenu

# configure taskwarrior
localhost-taskwarrior:
    just playbook localhost-taskwarrior

# configure syncthing
localhost-syncthing:
    just playbook localhost-syncthing

# run all localhost playbooks
localhost-all:
    just localhost-st
    just localhost-cli
    just localhost-i3
    just localhost-gpg
    just localhost-dmenu

# configure qbittorrent on nas
nas-qbittorrent:
    just playbook nas-qbittorrent

# configure samba on nas
nas-samba:
    just playbook nas-samba

# configure syncthing on nas
nas-syncthing:
    just playbook nas-syncthing

# run all nas playbooks
nas-all:
    just nas-qbittorrent
    just nas-samba
    just nas-syncthing
