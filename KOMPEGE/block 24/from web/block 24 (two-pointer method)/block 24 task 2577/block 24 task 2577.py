s = open("24_2577.txt").readline()

m = 0
l = 0
kt = 0
ky = 0

for r in range(len(s)):
    if s[r] == "Y":
        l = r + 1
        kt = 0
    if s[r] == ".":
        kt += 1
    if kt <= 5:
        m = max(m, r-l+1)
print(m)

# 208