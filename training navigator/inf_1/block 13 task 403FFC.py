from ipaddress import *



for mask in range(16, 33):
    ipA = ip_address("117.191.160.0")
    ip = ip_address("117.191.176.37")
    net = ip_network(f"{ip}/{mask}", 0)
    if net[0] == ipA:
        print(net.netmask)

# 224