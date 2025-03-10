from math import *

for kod in range(2, 1000):
    char = ceil(log2(kod))
    num = ceil(1231 * char/8)
    if 523872 * num > 432*1024*1024:
        print(kod)
        break