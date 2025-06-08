s = open("24_2427.txt").readline()

m = [1] * len(s)

for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        m[i] = m[i - 1] + 1

mx = max(m)

for i in range(1, len(s)):
    if m[i] == mx:
        print(s[i-mx+1:i+1])

# zrqjWRC1