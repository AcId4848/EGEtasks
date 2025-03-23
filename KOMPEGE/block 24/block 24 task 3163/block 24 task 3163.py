s = open("24_3163.txt").readline()
s1 = s.replace("PR", "P R").split()
s2 = s.replace("ST", "S T").split()

print(max(max(len(c) for c in s1), max(len(c1) for c1 in s2)))