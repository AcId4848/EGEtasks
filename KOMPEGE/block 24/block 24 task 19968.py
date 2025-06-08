from re import *

s = open("24_19968.txt").readline()

num = r"(?:[1-5][0-5]*|0)"

pattern = rf"{num}([+*]{num})*"

print(max([len(x.group()) for x in finditer(pattern, s)]))

# 26