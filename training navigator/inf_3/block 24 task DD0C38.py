s = open("DD0C38.txt").readline()

k = l = 0
m = 10000000

for r in range(len(s)):
    if "W" == s[r]:
        k += 1
    while k >= 240:
        m = min(m, r-l+1)
        if s[l] == "W":
            k -= 1
        l += 1

print(m)
# 624