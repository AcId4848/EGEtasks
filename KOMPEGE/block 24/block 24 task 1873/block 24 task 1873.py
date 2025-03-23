s = open("24_1873.txt").readline()
s = s.replace("PR", "P R").replace("RP", "R P").split()
print(max(len(c) for c in s))