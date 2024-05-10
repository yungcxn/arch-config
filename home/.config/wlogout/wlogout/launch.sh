#!/usr/bin/env bash

LAYOUT="$HOME/.config/wlogout/layout"
STYLE="$HOME/.config/wlogout/style.css"

if [[ ! `pidof wlogout` ]]; then
    wlogout --layout ${LAYOUT} --css ${STYLE} -p layer-shell
else
    pkill wlogout
fi
