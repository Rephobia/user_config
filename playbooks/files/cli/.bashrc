# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# ---- Aliases ----
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -lah'

# ---- Prompt ----
PS1='[\u@\h \W]\$ '

# ---- Custom aliases ----
# (сюда можно добавлять всякие полезные мелочи типа alias g=git и т.д.)
