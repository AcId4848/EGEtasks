from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f"148.195.140.28/{mask}", 0)
    print(net)
# 22