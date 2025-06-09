s = open("4D2418.txt").readline()

s = s.replace("XZZY", " ").split()

print(max([len(i) for i in s]) + 6)
# 1713