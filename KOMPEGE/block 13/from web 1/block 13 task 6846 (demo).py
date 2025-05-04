from ipaddress import ip_network

k = 0
net = ip_network("184.178.54.144/255.255.255.240")
for ip in net:
    b = f"{ip:b}"
    if "111" in b:
        k += 1

print(k) # 16