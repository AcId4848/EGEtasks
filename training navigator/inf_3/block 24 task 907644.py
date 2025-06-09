s = open("907644.txt").readline()

s = s.replace("CA", "*").replace("CB", "*").replace("A", " ").replace("B", " ").replace("C", " ").split()
print(len(max(s)))
# 78