s = open("98C518.txt").readline()

s = s.replace("AD", "A D").replace("DA", "D A").split()

print(max([len(i) for i in s]))
# 89