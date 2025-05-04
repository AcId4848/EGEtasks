from ipaddress import ip_network

for mask in range(33):
    net = ip_network(f"158.116.11.146/{mask}", 0)
    if "158.116.0.0" in str(net):
        print(net)
# 7