s = [int(f) for f in open("17_2402.txt")]

arr = []
for i in range(len(s) - 2):
    if s[i] % 3 == 2 or s[i + 1] % 3 == 2 or s[i + 2] % 3 == 2:
        arr.append(min(s[i], s[i+1], s[i+2]))

print(len(arr), sum(arr))
# 91 2627