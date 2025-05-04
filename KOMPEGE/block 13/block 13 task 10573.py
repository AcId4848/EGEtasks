from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f"191.173.145.240/{mask}", 0)
    if "191.173.144.0" in str(net):
        print(net.num_addresses)

# 512