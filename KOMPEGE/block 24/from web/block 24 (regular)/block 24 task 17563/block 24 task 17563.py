from re import *

s = open("24_17563.txt").readline()

num = r"[7-9][0, 7-9]*"

reg = rf"{num}([*-]{num})+"

m = max([x.group() for x in finditer(reg, s)], key = len)

print(len(m), m)

# 40