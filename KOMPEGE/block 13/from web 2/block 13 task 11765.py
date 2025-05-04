from ipaddress import *



ip = ip_address('130.140.241.137')
net = ip_address('130.140.240.0')

for mask in range(33):
   network = ip_network(f'{ip}/{mask}', 0)
   # print(mask, f"{net:b}", f"{network.network_address:b}")
   if network.network_address == net:
       print(mask, net, network.network_address)

# 23
