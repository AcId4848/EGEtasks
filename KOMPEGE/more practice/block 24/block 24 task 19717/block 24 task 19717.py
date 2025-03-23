s = open("24.5_19717.txt").readline()
s = s.split("M")
m = 0
for i in range(len(s)-3):
    c = "M".join(s[i:i+279])
    m = max(m, len(c))
print(m)