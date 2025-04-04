s = open("24_3020.txt").readline()
s = s.replace("ZX", "*").replace("ZY", "*").replace("X", " ").replace("Y", " ").replace("Z", " ").split()
print(max(len(c) for c in s))