s = open("24_10105.txt").readline()

l = m = k = 0

for r in range(len(s)):
    if s[r] == "T":
        k += 1
    while k > 100:
        if s[l] == "T":
            k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)

# 133
