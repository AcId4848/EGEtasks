from ipaddress import ip_network


for mask in range(33):
    net = ip_network(f"173.103.25.118/{mask}", 0)
    if "173.103.24.0" in str(net):
        print(net)

# 11