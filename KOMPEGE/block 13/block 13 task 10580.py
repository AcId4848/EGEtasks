from ipaddress import ip_network

net = ip_network("10.48.96.0/255.255.240.0")
print(len([ip for ip in net if f"{ip:b}".count("1") > f"{ip:b}".count("0")]))
# 13