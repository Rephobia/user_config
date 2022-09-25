default:
    just --list

venv:
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

# configure st
local-st: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/local-st.yaml --vault-password-file .ansible_vault

# configure cli (.bashrc, .inputrc)
local-cli: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/local-cli.yaml --vault-password-file .ansible_vault

# configure i3wm
local-i3: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/local-i3.yaml --vault-password-file .ansible_vault

# configure qbittorrent on nas
nas-qbittorrent: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/nas-qbittorrent.yaml --vault-password-file .ansible_vault

# configure samba on nas
nas-samba: venv
    ./venv/bin/ansible-playbook -i inventory.yaml playbooks/nas-samba.yaml --vault-password-file .ansible_vault

# configure nas
nas-configure: nas-qbittorrent nas-samba
