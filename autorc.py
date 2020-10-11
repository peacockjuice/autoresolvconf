import os

file = os.path.abspath("/etc/resolv.conf")
f = open(file,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("nameserver 127.0.0.53","nameserver 10.3.0.2\nnameserver 127.0.0.53\n")

f = open(file,'w')
f.write(newdata)
f.close()
