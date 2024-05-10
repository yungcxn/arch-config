#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias hyprconfig='nvim ~/.config/hypr/hyprland.conf'
alias hyprthemeconfig='nvim ~/.config/hypr/hyprland-theme.conf'
alias config='cd ~/.config'
alias tugba='cat ~/.config/ascii_art/bf_color.txt'

