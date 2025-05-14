from re import *

s = open("24_2423.txt").readline()

reg = r"(?=(0*1*2*3*4*5*6*7*8*9*))"

# print([x.group(1) for x in finditer(reg, s[:50])])
print(max(len(x.group(1)) for x in finditer(reg, s) if x.group(1).count("0") <= 1 and x.group(1).count("1") <= 1 and x.group(1).count("2") <= 1 and x.group(1).count("3") <= 1 and x.group(1).count("4") <= 1 and x.group(1).count("5") <= 1 and x.group(1).count("6") <= 1 and x.group(1).count("7") <= 1 and x.group(1).count("8") <= 1 and x.group(1).count("9") <= 1))
# 8
