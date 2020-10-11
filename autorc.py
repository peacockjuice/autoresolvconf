import os

file = os.path.abspath("/etc/resolv.conf")
f = open(file,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("nameserver %X-ip%","nameserver %Y-ip%\nnameserver %X-ip%\n")

f = open(file,'w')
f.write(newdata)
f.close()
