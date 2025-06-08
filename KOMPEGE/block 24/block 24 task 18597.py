from re import *

s = open("24_18597.txt").readline()

reg = r"([1-9]{1}[0-9]{3}\.[1-9]+[0-9]*&[1-9]{1}[0-9]{3}\.[1-9]+[0-9]*)+"


print(max([len(x.group()) for x in finditer(reg, s)]))
print(max([x.group() for x in finditer(reg, s)]))

# 45