s = open("24_2419.txt").readline()
s = s.replace("A", " ").replace("B", " ")
s = s.split()
print(max(len(c) for c in s))