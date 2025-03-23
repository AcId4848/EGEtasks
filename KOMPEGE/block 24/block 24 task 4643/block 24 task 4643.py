s = open("24_4643.txt").readline()
s = s.replace("B", "A").replace("2", "1").replace("11A", "*").replace("1", " ").replace("A", " ").split()
print(max(len(c) for c in s))
