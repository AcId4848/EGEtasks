from ipaddress import ip_network, ip_address


for mask in range(16, 33):
    ip = ip_address("57.179.208.27")
    ipA = ip_address("57.179.192.0")
    net = ip_network(f"{ip}/{mask}", 0)
    if net[0] == ipA:
        print(f"{net.netmask:b}".count("1"))

# 19