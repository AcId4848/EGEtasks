from re import *

s = open("24_19968.txt").readline()

num = "([1-5][0-5]*|0)"

# test

# print(s[:50])
# print([x.group() for x in finditer(num, s[:50])])

reg = rf"{num}([+*]{num})+"
m = max([x.group() for x in finditer(reg, s)], key=len)
print(len(m), m)

# 26