s = open("B92F00.txt").readline()

s = s.replace("AB", "A B").replace("BA", "B A").split()

print(max([len(i) for i in s]))
# 102