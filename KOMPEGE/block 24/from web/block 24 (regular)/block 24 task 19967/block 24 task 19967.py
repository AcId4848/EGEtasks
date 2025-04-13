from re import *

s = open("24_19967.txt").readline()

num = r"([1-9][0-9]*|0)"

reg = rf"AFD{num}([+*]{num})+"

m = max([x.group() for x in finditer(reg, s)], key=len)

print(len(m), m)

# 72