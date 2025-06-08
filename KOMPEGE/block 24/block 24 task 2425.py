from re import *

s = open("24_2425.txt").readline()

reg = r"(DBAC)+DBA"

print(max([len(x.group()) for x in finditer(reg, s)]))
# 95
