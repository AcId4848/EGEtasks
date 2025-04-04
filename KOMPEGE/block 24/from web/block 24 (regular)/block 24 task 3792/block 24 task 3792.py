from re import *

s = open("24_3792.txt").readline()

reg = r"[ABC]+"

print(max([len(x.group()) for x in finditer(reg, s)]))

# 16



