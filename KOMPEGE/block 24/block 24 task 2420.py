from re import *

s = open("24_2420.txt").readline()

reg = r"(?=([ABEF]+))"

print(s[:50])
print([x.group(1) for x in finditer(reg, s[50:])])
print(max(len(x.group(1)) for x in finditer(reg, s)))

# 20