from ipaddress import ip_network, ip_address

for mask in range(16, 25):
    ip = ip_address("152.65.245.132")
    net = ip_network(f"{ip}/{mask}", 0)
    if all(f"{ip:b}"[:16].count("0") >= f"{ip:b}"[16:].count("0") for ip in net):
        print(net.netmask)

# 252