s = open("24_7016.txt").readline()

m = 0
l = 0

for r in range(len(s)):
    if s[r] == "A" or s[r] == "D":
        if s[l] == "A" and s[r] == "D" or s[l] == "D" and s[r] == "A":
            m = max(m, r-l+1)
        l = r
print(m)
# 273