def yellowText(input):
    print("\033[33m" + input + "\033[m")

yellowText("Creating temporary install directory")
print("mkdir ./installTemp")
for deb in debs:
   yellowText("Installing " + deb[1])
   print("wget -O %s.deb %d" %(deb[2], deb[0]))