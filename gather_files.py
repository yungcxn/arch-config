'''
Copyright (c) yungcxn

This file is ran by me on my Arch Linux Installation to gather all config files

'''

import os

HOME_LOC = os.path.expanduser("~")
DOTCONFIG_LOC = HOME_LOC + "/.config"
ETC_LOC = "/etc"


cmap = [
  "home",
  "home/.config",
  "etc",
]

#single files
gather_from_to = {
  DOTCONFIG_LOC + "/alacritty": cmap[1] + "/alacritty",
  DOTCONFIG_LOC + "/nvim": cmap[1] + "/nvim",
  DOTCONFIG_LOC + "/zsh": cmap[1] + "/zsh",
  DOTCONFIG_LOC + "/wlogout": cmap[1] + "/wlogout",
  DOTCONFIG_LOC + "/hypr": cmap[1] + "/hypr",
  DOTCONFIG_LOC + "/wallpapers": cmap[1] + "/wallpapers",
  DOTCONFIG_LOC + "/waybar": cmap[1] + "/waybar",
  DOTCONFIG_LOC + "/ascii_art": cmap[1] + "/ascii_art",
  DOTCONFIG_LOC + "/wofi": cmap[1] + "/wofi",
  DOTCONFIG_LOC + "/Thunar": cmap[1] + "/Thunar",
  HOME_LOC + "/.vim": cmap[0] + "/.vim",
  HOME_LOC + "/.vimrc": cmap[0] + "/.vimrc",
  HOME_LOC + "/.oh-my-zsh": cmap[0] + "/.oh-my-zsh",
  HOME_LOC + "/.icons": cmap[0] + "/.icons",
  HOME_LOC + "/.themes": cmap[0] + "/.themes",
  ETC_LOC + "/greetd": cmap[2] + "/greetd",
}

gather_singles = {
  HOME_LOC + "/.zshrc": cmap[0] + "/.zshrc",
  HOME_LOC + "/.bashrc": cmap[0] + "/.bashrc",
  HOME_LOC + "/.p10k.zsh": cmap[0] + "/.p10k.zsh",
  DOTCONFIG_LOC + "/startup.sh" : cmap[1] + "/startup.sh",
  DOTCONFIG_LOC + "/user-dirs.dirs" : cmap[1] + "/user-dirs.dirs",
  DOTCONFIG_LOC + "/user-dirs.locale" : cmap[1] + "/user-dirs.locale",
}

# create non existing folder with recursion
def create_folder(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

# change cwd to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# create the folder to store the files, gather_from_to values
for value in gather_from_to.values():
  create_folder(value)

# copy files from gather_from_to from keys to values
for key, value in gather_from_to.items():
  os.system(f'cp -r {key} {value}')

# copy files from gather_singles from keys to values
for key, value in gather_singles.items():
  os.system(f'cp {key} {value}')


# add all created files and directorys to git
os.system('git add .')

# print git status
os.system('git status')
