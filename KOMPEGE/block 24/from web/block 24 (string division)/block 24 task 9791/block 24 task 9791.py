s = open("24_9791.txt").readline()
for c in "QWRTYUIOPSGHJKLZXVNM":
    s = s.replace(c, " ")
print(max(len(i) for i in s.split()))