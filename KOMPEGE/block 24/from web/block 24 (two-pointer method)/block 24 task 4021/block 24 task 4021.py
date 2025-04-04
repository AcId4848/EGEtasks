s = open("24_4021.txt").readline()
l = 0
m = 0
k = 0

for r in range(len(s)):
    if s[r] == ".":
        k += 1
    while k > 5:
        if s[l] == '.':
            k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)
# 550