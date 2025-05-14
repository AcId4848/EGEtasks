from re import *

s = open("24_2422.txt").readline()

reg = r"(?=(X+Y+Z+))"

# print([x.group(1) for x in finditer(reg, s[:50])])
print(max(len(x.group(1)) for x in finditer(reg, s)))
# 15