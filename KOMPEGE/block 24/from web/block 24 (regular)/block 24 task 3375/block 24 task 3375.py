from re import *

s = open("24_3375.txt").readline()

reg = r"(?=((AA|CC)+))"

print(s[:50])
print([x.group(1) for x in finditer(reg, s[:50])])
print(max(len(x.group(1)) // 2 for x in finditer(reg, s)))

# 5