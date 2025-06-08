from ipaddress import ip_network, ip_address

for mask in range(16, 32):
    ipA = ip_address("220.127.160.0")
    ip = ip_address("220.127.169.23")
    net = ip_network(f"{ip}/{mask}", 0)
    if net[0] == ipA:
        print(f"{net.netmask:b}".count("1"))

# 19