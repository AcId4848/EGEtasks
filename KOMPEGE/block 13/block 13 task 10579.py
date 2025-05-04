from ipaddress import ip_network

net = ip_network(f"192.168.240.0/255.255.255.0", 0)
print(len([f"{ip:b}" for ip in net if f"{ip:b}".count("0") == f"{ip:b}".count("1")]))
# 8
