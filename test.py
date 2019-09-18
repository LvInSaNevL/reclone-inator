import shutil
import os

gnomeSettings = ["desktop.background show-desktop-icons false",
                 "desktop.background picture-uri file:///%s/backgrounds/Enceladus.png" %(os.getcwd()),
                 "shell.extensions.dash-to-dock dock-position BOTTOM",
                 "shell favorite-apps \"['org.gnome.Terminal.desktop', 'org.gnome.Nautilus.desktop', 'firefox.desktop', 'discord-canary.desktop', 'code-insiders.desktop']\""]

for setting in gnomeSettings:
    os.system("gsettings set org.gnome.%s" %setting)