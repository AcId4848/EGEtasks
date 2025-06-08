from re import *

s = open("24_5171.txt").readline()

reg = r"(CA)+"

print(max([len(x.group()) for x in finditer(reg, s)]))
# 54
