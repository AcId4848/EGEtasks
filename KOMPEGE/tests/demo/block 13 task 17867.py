from ipaddress import ip_network

net = ip_network("172.16.168.0/255.255.248.0", 0)

count = 0
for ip in net:
    if f"{ip:b}".count("1") % 5 != 0:
        count += 1

print(count)