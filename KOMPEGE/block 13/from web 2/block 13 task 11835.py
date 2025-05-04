from ipaddress import ip_network, ip_address

k = 0
for A in range(256):
    ip = ip_address(f"207.0.{A}.167")
    net = ip_network(f"{ip}/255.255.255.192", 0)
    if all(f"{ip:b}"[:16].count("0") > f"{ip:b}"[16:].count("0") for ip in net) and \
        net[0] < ip < net[-1]:
        k += 1

print(k)
# 37
print(f"{192:b}")
print(f"{167:b}")