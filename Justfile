# list of all justfile recipes
default:
    just --list --unsorted

# create python virtual environment for ansible
venv:
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

# run playbook by name
playbook playbook: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/{{playbook}}.yaml --vault-password-file .ansible_vault

# configure st
local-st:
    just playbook local-st

# configure cli (.bashrc, .inputrc)
local-cli:
    just playbook local-cli

# configure i3wm
local-i3:
    just playbook local-i3

# run all local playbooks
local-all:
    just local-st
    just local-cli
    just local-i3

# configure qbittorrent on nas
nas-qbittorrent:
    just playbook nas-qbittorrent

# configure samba on nas
nas-samba: venv
    just playbook nas-samba

# run all nas playbooks
nas-all:
    just nas-qbittorrent
    just nas-samba
