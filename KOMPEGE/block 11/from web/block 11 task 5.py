from math import *

for k in range(1, 1000):
    kod = 10 + 52 + 1988
    char = ceil(log2(kod))
    num = ceil(k*char/8)
    if 1974 * num <= 579 * 1024:
        print(k)