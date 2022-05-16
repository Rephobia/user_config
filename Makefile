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
