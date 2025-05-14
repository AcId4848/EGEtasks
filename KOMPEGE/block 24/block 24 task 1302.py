s = open("24_1302.txt").readline()

s = s.replace("XZZY", " ")

print(max(len(c) for c in s.split()) + 6)
# 1713