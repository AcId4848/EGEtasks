from ipaddress import ip_network, ip_address

for mask in range(16, 32):
    ipA = ip_address("208.240.112.192")
    ip = ip_address("208.240.112.208")
    net = ip_network(f"{ip}/{mask}", 0)
    if net[0] == ipA:
        print(net.netmask)

# 192