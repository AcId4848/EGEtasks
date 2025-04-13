from re import *

s = open("24_7094.txt").readline()

reg = r"([CDF][AU])+"

print(max(len(x.group())//2 for x in finditer(reg, s)))
# 173

