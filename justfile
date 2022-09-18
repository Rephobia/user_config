default:
    just --list

venv:
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

# configure local system
local-build: venv
    ./venv/bin/python builder.py build

# configure local system
local-unbuild: venv
    ./venv/bin/python builder.py unbuild

# configure qbittorrent on nas
nas-configure-qbittorrent: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/qbittorrent.yaml --vault-password-file .ansible_vault

# configure samba on nas
nas-configure-samba: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/samba.yaml --vault-password-file .ansible_vault
