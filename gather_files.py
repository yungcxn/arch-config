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
  DOTCONFIG_LOC + "/alacritty": cmap[1],
  DOTCONFIG_LOC + "/nvim": cmap[1],
  #DOTCONFIG_LOC + "/zsh": cmap[1],
  DOTCONFIG_LOC + "/wlogout": cmap[1],
  DOTCONFIG_LOC + "/hypr": cmap[1],
  DOTCONFIG_LOC + "/wallpapers": cmap[1],
  DOTCONFIG_LOC + "/waybar": cmap[1],
  DOTCONFIG_LOC + "/ascii_art": cmap[1],
  DOTCONFIG_LOC + "/wofi": cmap[1],
  DOTCONFIG_LOC + "/Thunar": cmap[1],
  DOTCONFIG_LOC + "/qt5ct": cmap[1],
  DOTCONFIG_LOC + "/qt6ct": cmap[1],
  DOTCONFIG_LOC + "/mako": cmap[1],
  HOME_LOC + "/.vim": cmap[0],
  HOME_LOC + "/.vimrc": cmap[0],
  #HOME_LOC + "/.oh-my-zsh": cmap[0],
  #HOME_LOC + "/.icons": cmap[0],
  #HOME_LOC + "/.themes": cmap[0],
  ETC_LOC + "/greetd": cmap[2],
}

gather_singles = {
  HOME_LOC + "/.zshrc": cmap[0],
  HOME_LOC + "/.bashrc": cmap[0],
  HOME_LOC + "/.p10k.zsh": cmap[0],
  DOTCONFIG_LOC + "/startup.sh" : cmap[1],
  #DOTCONFIG_LOC + "/user-dirs.dirs" : cmap[1],
  #DOTCONFIG_LOC + "/user-dirs.locale" : cmap[1],
}

# create non existing folder with recursion
def create_folder(folder):
  if os.path.exists(folder):
      os.system(f'sudo rm -r {folder}')
  os.makedirs(folder)

# change cwd to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# create the folder to store the files, gather_from_to values
for value in gather_from_to.values():
  create_folder(value)

# copy files from gather_from_to from keys to values
for key, value in gather_from_to.items():
  os.system(f'sudo cp -r {key} {value}')

# copy files from gather_singles from keys to values
for key, value in gather_singles.items():
  os.system(f'sudo cp {key} {value}')

os.system('sudo chown -R can .')
