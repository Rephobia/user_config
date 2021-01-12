#!/bin/bash

application="$({ tac "$HOME/.hist"; compgen -ac | sort -u; } | perl -nE '$seen{$_}++ or print' | rofi -dmenu -p 'run' | tee -a "$HOME/.hist")"
i3-msg workspace $application
i3-msg exec $application
