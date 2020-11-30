#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export PATH
export EDITOR="nano"
export ALTERNATE_EDITOR=""
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -lah'
PS1='[\u@\h \W]\$ '
tty
