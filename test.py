import os
def yellowText(input):
    print("\033[33m" + input + "\033[m")

fstab = ["/dev/sda2	/mnt	auto	auto,nouser,exec,rw,async,atime	0 0"]

for mount in fstab:
    os.system("sudo su -c \"echo '%s' >> /etc/fstab\"" %(mount))