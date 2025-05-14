from re import *

s = open("24_1040.txt").readline()

reg = r"(?=([0123456789]+))"

print(s[50:])
print([x.group(1) for x in finditer(reg, s[50:])])
print(max(len(x.group(1)) for x in finditer(reg, s)))
# 12