s = open("24_6734.txt").readline()
s = s.split(".")
m = 10000
for i in range(len(s)-7):
    c = ".".join(s[i:i+8])
    m = min(m, len(c) - len(s[i]) - len(s[i+7]))
print(m)