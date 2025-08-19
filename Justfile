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

# run playbook by name with tags
playbook-with-tags playbook tags: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/{{playbook}}.yaml --vault-password-file .ansible_vault -t {{tags}}

# configure st
localhost-st:
    just playbook localhost-st

# configure cli (.bashrc, .inputrc)
localhost-cli:
    just playbook localhost-cli

# configure i3wm with desktop i3bar
localhost-i3-desktop:
    just playbook-with-tags localhost-i3 desktop
    
# configure i3wm with laptop i3bar
localhost-i3-laptop:
    just playbook-with-tags localhost-i3 laptop

# configure gpg
localhost-gpg:
    just playbook localhost-gpg

# configure dmenu
localhost-dmenu:
    just playbook localhost-dmenu

# configure syncthing
localhost-syncthing:
    just playbook localhost-syncthing

# configure (mount) samba with fstab
localhost-samba-fstab:
    just playbook localhost-samba-fstab
    
# configure (mount) samba with gio
localhost-samba-gio:
    just playbook localhost-samba-gio

# run all localhost playbooks
localhost-all:
    just localhost-st
    just localhost-cli
    just localhost-i3
    just localhost-gpg
    just localhost-dmenu
    just localhost-samba

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
