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

export GOPATH="$HOME/go"; export GOROOT="$HOME/.go"; export PATH="$GOPATH/bin:$PATH"; # g-install: do NOT edit, see https://github.com/stefanmaric/g

# Add $HOME/.cargo/bin to path binaries
export PATH="$PATH:$HOME/.cargo/bin"

[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc

alias t="task"
