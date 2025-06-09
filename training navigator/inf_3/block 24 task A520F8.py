s = open("A520F8.txt").readline()

s = s.replace("BD", "B D").replace("DB", "D B").split()
print(max([len(i) for i in s]))
# 104