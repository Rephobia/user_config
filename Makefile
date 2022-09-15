.PHONY: help
.DEFAULT_GOAL := help
SHELL := /bin/bash

ifneq (,$(wildcard ./.env))
    include .env
    export
endif

##
##COMMON COMMANDS
##

help: ## Shows list of commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//' | sed -E 's/(.*:)/\t\1/'

##
##HOST BUILD COMMANDS
##

venv: ## install python dependencies as virtual env
	python3 -m venv venv
	(source ./venv/bin/activate; pip install -r requirements.txt;)
build: ## build host environment
	./venv/bin/python builder.py build

unbuild: ## unbuild host environment
	./venv/bin/python builder.py unbuild

##
##SELF-HOSTED BUILD COMMANDS
##

nas-qbittorrent: ## build torrent environment
	(source ./venv/bin/activate; ansible-playbook -i inventory.yaml playbooks/qbittorrent.yaml --vault-password-file .ansible_vault)

nas-samba: ## build samba environment
	(source ./venv/bin/activate; ansible-playbook -i inventory.yaml playbooks/samba.yaml --vault-password-file .ansible_vault)
