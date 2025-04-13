from re import *

s = open("24_17641.txt").readline()

num = r"([1-9][0-9]*|0)"

proiz = rf"({num}\*)*0(\*{num})*"

reg = rf"{proiz}(\+{proiz})+"

m = max([x.group() for x in finditer(reg, s)], key=len)
print(len(m), m)

# 142