s = [int(x) for x in open("17_17873.txt")]


ans = []
for i in range(len(s) - 1):
    if s[i] % 16 == min(s) or s[i+1] % 16 == min(s):
       ans.append(s[i] + s[i+1])

print(len(ans), max(ans))