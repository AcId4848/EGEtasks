from re import *

s = open("24_4643.txt").readline()

reg = r"([12][12][AB])+"
print(max(len(x.group())//3 for x in finditer(reg, s)))
# 67