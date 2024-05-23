#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias hyprconfig='cd ~/.config/hypr'
alias config='cd ~/.config'
# alias tugba='cat ~/.config/ascii_art/bf_color.txt'
alias tugba='python3 ~/Documents/quickquran/quickquran.py -r -t 1'
alias vpnon='sh ~/.config/vpn/start.sh'
alias vpnoff='sh ~/.config/vpn/stop.sh'

