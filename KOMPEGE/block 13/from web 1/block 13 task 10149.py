from ipaddress import *

for mask in range(33):
    net = ip_network(f"220.128.112.142/{mask}", 0)
    if str(net[0]) == "220.128.96.0":
        print(int((int(str(net)[-2:])-16)*"1" + (8 - (int(str(net)[-2:])-16))*"0", 2))
        print(net.netmask)

# 224