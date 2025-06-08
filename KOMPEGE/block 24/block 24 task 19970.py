from re import *

s = open("24_19970.txt").readline()

num = r"(?:[1-9][0-9]*[0,5]|0)"

pattern = rf"{num}([+*]{num})*"

print(max([len(x.group()) for x in finditer(pattern, s)]))
# 91