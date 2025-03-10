from math import log2, ceil

kod = 10 + 4090
char = ceil(log2(kod))
idd = ceil(101 * char / 8)
print(2048 * idd / 1024)