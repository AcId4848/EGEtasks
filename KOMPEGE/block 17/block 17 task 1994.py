s = [int(f) for f in open("17_1994.txt")]

arr = []
for i in range(len(s)-1):
    if s[i] * s[i+1] > 0 and (s[i] + s[i+1]) % 7 == 0:
        arr.append(s[i] * s[i+1])


print(len(arr), min(arr))
# 359 115022