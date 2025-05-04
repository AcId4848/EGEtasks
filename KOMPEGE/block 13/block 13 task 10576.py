from ipaddress import ip_network

net = ip_network("192.192.0.0/255.255.240.0", 0)
print(net.num_addresses-2)
# 4094