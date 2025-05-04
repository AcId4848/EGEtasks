from ipaddress import ip_network

k = 0
net = ip_network("211.48.136.64/255.255.255.224")
for ip in net:
    b = f"{ip:b}"
    if b[-2:] == "11":
        k += 1

print(k)
# 8