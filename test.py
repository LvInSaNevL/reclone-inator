import shutil
import os

aliases = ["# Custom Aliases",
           "alias mcstart='java -Xmx1024M -Xms1024M -jar server_1.1.4.jar nogui'",
           "alias update='sudo apt-get update && sudo apt-get upgrade'",
           "alias ip='echo \"Local IP:    $(hostname -i)\" && echo \"External IP: $(wget -qO- http://ipecho.net/plain | xargs echo)\"',
           "alias cpv='rsync -ah --info=progress2'"
           "qemu(){ qemu-system-x86_64 -boot d -cdrom $1 -m 1024; }"]

for alias in aliases:
    os.system("sudo echo '%s' >> ~/.bashrc" %alias)