from ipaddress import ip_network


for mask in range(33):
    net = ip_network(f"175.122.80.13/{mask}", 0)
    if "175.122.80.0" in str(net) and net.num_addresses > 60:
        print(net, net.num_addresses)
# 7