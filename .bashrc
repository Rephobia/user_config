#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

expt PATH
expt EDITOR="nano"
expt ALTERNATE_EDITOR=""
alias ls='ls --col=auto'
alias grep='grep --col=auto'
alias ll='ls -lah'
PS1='[\u@\h \W]\$ '
tty
