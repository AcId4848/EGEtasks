from re import *

s = open("24_2426.txt").readline()

reg = r"(?=([123]+))"

print(s[:50])
print([x.group(1) for x in finditer(reg, s[50:])])
print(max(len(x.group(1)) for x in finditer(reg, s)))
# 20