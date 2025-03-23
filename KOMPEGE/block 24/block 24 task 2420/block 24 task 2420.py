s = open("24_2420.txt").readline()
s = s.replace("C", " ").replace("D", " ")
s = s.split()
print(max(len(c) for c in s))