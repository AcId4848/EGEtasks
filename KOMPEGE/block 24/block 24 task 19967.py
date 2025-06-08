from re import *

s = open("24_19967.txt").readline()

num = r"(?:[1-9][0-9]*|0)"

pattern = rf"AFD{num}([+*]{num})*"

print(max([x.group() for x in finditer(pattern, s)]))

# 72