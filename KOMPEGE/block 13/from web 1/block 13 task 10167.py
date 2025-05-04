from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f"108.133.75.91/{mask}", 0)
    print(net, net.num_addresses)

# 64