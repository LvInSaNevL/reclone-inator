import os
def yellowText(input):
    print("\033[33m" + input + "\033[m")

# PPAs that I need
repos = ["ppa:lyzardking/ubuntu-make",
         "ppa:ubuntu-mozilla-daily/firefox-aurora"]

# APT install list
aptPacks = ["ubuntu-gnome-desktop --no-install-recommends",
            "build-essential",
            "gparted",
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
            "libicu60",]

# Snap packages
snapPacks = ["okular",
            "dotnet-sdk && sudo snap alias dotnet-sdk.dotnet dotnet"]

# Debian Archives
debs = [["https://discordapp.com/api/download/canary?platform=linux", "Discord Canary", "discord.deb"],
        ["https://go.microsoft.com/fwlink/?LinkID=760865", "VS Code Insiders", "vscode.deb"],
        ["https://steamcdn-a.akamaihd.net/client/installer/steam.deb", "Steam", "steam.deb"]]

manualInstalls = ["https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.AppImage"]

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
   os.system("wget -O %s %s" %(deb[2], deb[0]))
   os.system("dpkg -i %s" %deb[2])
yellowText("Cleaning up install files")
os.system("rm -rv ./installTemp")

yellowText("Fixing and removing packages")
os.system("sudo apt install --fix-broken -y && sudo apt autoremove")

yellowText("Updating the system")
os.system("sudo apt update && sudo apt upgrade")

# Reboots the system
input("Press any key to reboot the system")
os.system("reboot")