s = open("F04010.txt").readline()

k = l = 0
m = 10000000

for r in range(len(s)):
    if "Y" == s[r]:
        k += 1
    while k >= 260:
        m = min(m, r - l + 1)
        if "Y" == s[l]:
            k -= 1
        l += 1


print(m)
# 817