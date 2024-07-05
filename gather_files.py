import os

HOME_LOC = "/home/can"
DOTCONFIG_LOC = HOME_LOC + "/.config"
ETC_LOC = "/etc"
GTK_THEMES_LOC = "/usr/share/themes/"

cmap = {
    "home": "./home/",
    "config": "./home/.config/",
    "etc": "./etc/",
    "themes": "./usr/share/themes/"
}

# Config files and directories to gather
gather_from_to = {
    DOTCONFIG_LOC + "/alacritty/": cmap["config"],
    DOTCONFIG_LOC + "/nvim/": cmap["config"],
    #DOTCONFIG_LOC + "/zsh": cmap["config"],
    DOTCONFIG_LOC + "/wlogout/": cmap["config"],
    DOTCONFIG_LOC + "/hypr/": cmap["config"],
    DOTCONFIG_LOC + "/wallpapers/": cmap["config"],
    DOTCONFIG_LOC + "/waybar/": cmap["config"],
    DOTCONFIG_LOC + "/ascii_art/": cmap["config"],
    DOTCONFIG_LOC + "/wofi/": cmap["config"],
    DOTCONFIG_LOC + "/Thunar/": cmap["config"],
    DOTCONFIG_LOC + "/qt5ct/": cmap["config"],
    DOTCONFIG_LOC + "/qt6ct/": cmap["config"],
    DOTCONFIG_LOC + "/mako/": cmap["config"],
    HOME_LOC + "/.vim/": cmap["home"],
    #HOME_LOC + "/.oh-my-zsh": cmap["home"],
    #HOME_LOC + "/.icons": cmap["home"],
    #HOME_LOC + "/.themes": cmap["home"],
    ETC_LOC + "/greetd/": cmap["etc"],
    GTK_THEMES_LOC: cmap["themes"]
}

# Single files to gather
gather_singles = {
    HOME_LOC + "/.zshrc": cmap["home"],
    HOME_LOC + "/.bashrc": cmap["home"],
    HOME_LOC + "/.p10k.zsh": cmap["home"],
    DOTCONFIG_LOC + "/startup.sh": cmap["config"],
    HOME_LOC + "/.vimrc": cmap["home"],
    #DOTCONFIG_LOC + "/user-dirs.dirs": cmap["config"],
    #DOTCONFIG_LOC + "/user-dirs.locale": cmap["config"],
}

# Create non-existing folders
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Change to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create destination directories
for value in set(gather_from_to.values()):
    create_folder(value)

# Copy directories
for src, dst in gather_from_to.items():
    os.system(f'sudo cp -r {src} {dst}')

# Copy single files
for src, dst in gather_singles.items():
    os.system(f'sudo cp {src} {dst}')

# Remove large video files
for root, _, files in os.walk("."):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) > 100000000:
            os.system(f'sudo rm {file_path}')
            print(f"Removed {file_path}")

# Change ownership
os.system("sudo chown -R can:can .")