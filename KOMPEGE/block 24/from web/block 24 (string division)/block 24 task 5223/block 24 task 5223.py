s = open("24_5223.txt").readline()
s = s.replace("DD", "D D").split()
s = [c for c in s if "FE" in c]
print(max(len(i) for i in s))