s = open("24_21.txt").readline()

s = s.replace("XX", "X X").replace("YY", "Y Y").replace("ZZ", "Z Z").replace("XX", "X X").replace("YY", "Y Y").replace("ZZ", "Z Z")
s = s.split()

print(max(len(x) for x in s))
# 35