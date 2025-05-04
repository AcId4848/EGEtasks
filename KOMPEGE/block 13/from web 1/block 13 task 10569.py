from ipaddress import *

a = [10, 8, 248, 131]
b = [255, 255, 224, 0]
c = [a[i] & b[i] for i in range(4)]
print(".".join(str(i) for i in c))

net = ip_network("10.8.248.131/255.255.224.0", 0)
print(net)
# 224