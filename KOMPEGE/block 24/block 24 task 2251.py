s = open("24_2251.txt").readline()

l = m = k = 0

for r in range(len(s)):
    if s[r] == "D":
        k += 1
    while k > 2:
        if s[l] == "D":
            k -= 1
        l += 1
    m = max(m, r-l+1)
print(m)