import os
def yellowText(input):
    print("\033[33m" + input + "\033[m")

fstab = ["//bistack/vault      /mnt/Network_Shares/Vault      cifs username={},password={},noperm,iocharset=utf8 0 0",
         "//bistack/matt       /mnt/Network_Shares/Matt       cifs username={},password={},noperm,iocharset=utf8 0 0",
         "//bistack/cadosphere /mnt/Network_Shares/Cadosphere cifs username={},password={},noperm,iocharset=utf8 0 0"]

username = raw_input("What is your Bistack username; ")
password = raw_input("What is your Bistack password; ")
print("sudo su -c \"echo '/dev/sda2	       /mnt           	              auto auto,nouser,exec,rw,async,atime	             0 0' >> /etc/fstab")
for mount in fstab:
    mountCreds = mount.format(username, password)
    print("sudo su -c \"echo '{}' >> /etc/fstab".format(mount.format(username, password)))