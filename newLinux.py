import os
import shutil

def yellowText(input):
    print("\033[33m" + input + "\033[m")

# PPAs that I need
repos = ["ppa:lyzardking/ubuntu-make",
        "ppa:ubuntu-mozilla-daily/firefox-aurora",
        "ppa:obsproject/obs-studio",
        "ppa:lutris-team/lutris",
        "deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main"]

# APT install list
aptPacks = ["ubuntu-gnome-desktop --no-install-recommends",
            "build-essential",
            "gparted",
            "gpart",
            "libgconf-2-4",
            "libappindicator1",
            "snapd",
            "gnome-tweaks",
            "dconf-editor",
            "libc6-i386",
            "libgl1-mesa-dri:i386",
            "libgl1-mesa-glx:i386",
            "libc6:i386",
            "vlc",
            "blender",
            "liblttng-ust0",
            "libcurl4",
            "libssl1.0.0",
            "libkrb5-3",
            "zlib1g",
            "libicu60",
            "speedtest-cli",
            "cifs-utils",
            "gimp",
            "ffmpeg"
            "obs-studio",
            "lutris",
            "firefox",
            "okular",
            "deluged",
            "deluge-web",
            "deluge-console",
            "deluge",
            "youtube-dl"]

# Snap packages
snapPacks = ["dotnet-sdk && sudo snap alias dotnet-sdk.dotnet dotnet"]

# Debian Archives
debs = [["https://discordapp.com/api/download/canary?platform=linux", "Discord Canary", "discord.deb"],
        ["https://go.microsoft.com/fwlink/?LinkID=760865", "VS Code Insiders", "vscode.deb"],
        ["https://steamcdn-a.akamaihd.net/client/installer/steam.deb", "Steam", "steam.deb"],
        ["https://launcher.mojang.com/download/Minecraft.deb", "Minecrat", "minecraft.deb"]]

manualInstalls = ["https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.AppImage"]

gnomeSettings = ["desktop.background show-desktop-icons false",
                 "desktop.background picture-uri file:///%s/backgrounds/Enceladus.png" %(os.getcwd()),
                 "shell.extensions.dash-to-dock dock-position BOTTOM",
                 "shell favorite-apps \"['org.gnome.Terminal.desktop', 'org.gnome.Nautilus.desktop', 'firefox.desktop', 'discord-canary.desktop', 'code-insiders.desktop', 'lutris.desktop']\""]

gameDrivers = ["add-apt-repository ppa:paulo-miguel-dias/pkppa -y",
                "dpkg --add-architecture i386",
                "apt update && sudo apt upgrade",
                "apt install libgl1-mesa-glx:i386 libgl1-mesa-dri:i386",
                "apt install mesa-vulkan-drivers mesa-vulkan-drivers:i386"]

aliases = ["# Custom Aliases",
           "alias mcstart='java -Xmx1024M -Xms1024M -jar server_1.1.4.jar nogui'",
           "alias update='sudo apt-get update && sudo apt-get upgrade'",
           "alias ip='echo \"Local IP:    $(hostname -i)\" && echo \"External IP: $(wget -qO- http://ipecho.net/plain | xargs echo)\"'",
           "alias cpv='rsync -ah --info=progress2'",
           "alias lock='xdg-screensaver lock'",
           "qemu(){ qemu-system-x86_64 -boot d -cdrom $1 -m 1024; }"]

# Adding repos
for ppa in repos:
    yellowText("Adding repository " + ppa)
    os.system("sudo add-apt-repository %s -y" %ppa)
yellowText("Updating apt list")
os.system("sudo apt update && sudo apt upgrade -y")
    
# Adding apt packages
for apt in aptPacks:
    yellowText("Installing " + apt)
    os.system("sudo apt install %s -y" %apt)

# Adding snap packages
for snap in snapPacks:
    yellowText("Installing " + snap)
    os.system("sudo snap install %s" %snap)

# Adding deb packages
yellowText("Creating temporary install directory")
os.system("mkdir ./installTemp")
for deb in debs:
   yellowText("Installing " + deb[1])
   os.system("wget -O ./installTemp/%s %s" %(deb[2], deb[0]))
   os.system("sudo dpkg -i ./installTemp/%s" %deb[2])
yellowText("Cleaning up install files")
os.system("rm -rv ./installTemp")

yellowText("Fixing and removing packages")
os.system("sudo apt install --fix-broken -y && sudo apt autoremove -y")

yellowText("Updating the system")
os.system("sudo apt update -y && sudo apt upgrade -y")

# Video drivers ( Currently for Intel drivers on Ubuntu 18.04)
yellowText("Installing video drivers")
for driver in gameDrivers:
    os.system("sudo %s" %driver)

# Quality of life changes (Network drives, gnome settings, VS Code settings, Bash Aliases)
for setting in gnomeSettings:
    os.system("gsettings set org.gnome.%s" %setting)
for alias in aliases:
    os.system("sudo echo '%s' >> ~/.bashrc" %alias)

# Reboots the system
input("Press any key to reboot the system")
os.system("systemctl reboot -i")
