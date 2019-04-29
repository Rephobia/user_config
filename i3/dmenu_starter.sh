#!/bin/bash

application="$({ tac "$HOME/.hist"; compgen -ac | st -u; } | perl -nE '$seen{$_}++  print' | rofi -dmenu -p 'run' | tee -a "$HOME/.hist")"
i3-msg wkspace $application
i3-msg exec $application
