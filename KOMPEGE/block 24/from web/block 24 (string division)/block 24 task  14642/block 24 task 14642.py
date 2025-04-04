s = open("24.3_14642.txt").readline()
s = s.split("F")
m = 0
for i in range(len(s)-1):
    c = s[i] + "F" + s[i + 1]
    m = max(m, len(c))
print(m)