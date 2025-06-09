s = open("685605.txt").readline()

s = s.replace("AC", "*").replace("BC", "*").replace("A", " ").replace("B", " ").replace("C", " ").split()

print(len(max(s)))
# 97