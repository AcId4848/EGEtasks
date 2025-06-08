from re import *

s = open("24_17878.txt").readline()

num = r"(?:[6-9][0, 6-9]*|0)"

pattern = rf"{num}([-*]{num})*"

print(max([len(x.group()) for x in finditer(pattern, s)]))