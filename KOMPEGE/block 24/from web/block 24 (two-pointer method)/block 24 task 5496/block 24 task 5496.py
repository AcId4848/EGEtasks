s = open("24_5496.txt").readline()

m = 0
l = s.find("O")
# l = 0
ko = 0

for r in range(l, len(s)):
    if s[r] == "O":
        ko += 1
    if s[r] == "D":
        if ko > 2:
            l = r
        ko = 0
    if s[l] == "D" and s[r] == "D":
        m = max(m, r-l+1)

print(m)