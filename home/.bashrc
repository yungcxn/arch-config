#
# ~/.bashrc
#
export JAVA_HOME=/usr/lib/jvm/default
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PATH="${PATH}:/home/can/.local/bin"

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias hyprconfig='cd ~/.config/hypr'
alias config='cd ~/.config'
# alias tugba='cat ~/.config/ascii_art/bf_color.txt'
alias tugba='python3 ~/Documents/quickquran/quickquran.py -r -t 1'
alias vpnon='sh ~/.config/vpn/start.sh'
alias vpnoff='sh ~/.config/vpn/stop.sh'
alias renew='cd /mnt/D/DEVELOPMENT/art/Renew/dist && java -p .:libs -m de.renew.loader gui'
alias vim='nvim'
alias c='code -n --ozone-platform=wayland --disable-gpu'
alias serverstop='sh ~/local-website/stop.sh'
alias serverstart='sh ~/local-website/start.sh'
alias renew='java -p /mnt/D/DEVELOPMENT/art/Renew/dist:libs -m de.renew.loader gui'
