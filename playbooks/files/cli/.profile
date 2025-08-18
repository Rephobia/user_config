# ~/.profile

# PATH
if [[ -d "$HOME/.local/bin" ]]; then
    PATH="$HOME/.local/bin:$PATH"
fi
if [[ -d "$HOME/bin" ]]; then
    PATH="$HOME/bin:$PATH"
fi

# Go
export GOPATH="$HOME/go"
export GOROOT="$HOME/.go"
PATH="$GOPATH/bin:$GOROOT/bin:$PATH"

# Rust
if [[ -d "$HOME/.cargo/bin" ]]; then
    PATH="$HOME/.cargo/bin:$PATH"
fi

# PHPBrew
[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc

# EDITORS
export EDITOR="nano"
export ALTERNATE_EDITOR=""
export LC_TIME=ru_RU.UTF-8
