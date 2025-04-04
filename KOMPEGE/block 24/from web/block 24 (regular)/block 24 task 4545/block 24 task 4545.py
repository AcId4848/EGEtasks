from re import *

s = open("24_4545.txt").readline()

reg = r"(XYZ|ZYX)+"

print(max([len(x.group()) // 3 for x in finditer(reg, s)]))

# 13