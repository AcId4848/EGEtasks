s = open("281D2A.txt").readline()

l = k = 0
m = 1000000

for r in range(len(s)):
    if "Z" == s[r]:
        k += 1
    while k >= 200:
        m = min(m, r-l+1)
        if s[l] == "Z":
            k -= 1
        l += 1

print(m)
# 388