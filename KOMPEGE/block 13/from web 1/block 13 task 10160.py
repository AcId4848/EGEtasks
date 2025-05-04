from ipaddress import ip_network

a = []
for mask in range(33):
    net = ip_network(f"76.155.48.2/{mask}", 0)
    if "76.155.48.0" in str(net):
        a.append(net)

print(len(a))
# 11