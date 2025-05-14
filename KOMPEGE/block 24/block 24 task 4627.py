from re import *

s = open("24_4627.txt").readline()

reg = r"(?=((NPO|PNO)+))"


# print(s[50:])
print([x.group(1) for x in finditer(reg, s[50:])])
print(max(len(x.group(1)) for x in finditer(reg, s)) // 3
# 327