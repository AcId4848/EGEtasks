from re import *

s = open("24_2428.txt").readline()

reg = r"YZ(XYZ)+X"

print(max(len(x.group()) for x in finditer(reg, s)))

# 69
