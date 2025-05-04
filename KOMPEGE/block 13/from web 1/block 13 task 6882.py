from ipaddress import ip_network

net = ip_network("192.168.0.0/255.255.128.0", 0)

k = 0
for ip in net:
    if int(ip) % 4 == 0:
        k += 1

print(k)
# 8192