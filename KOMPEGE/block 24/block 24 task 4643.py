s = open("24_4643.txt").readline()

s = s.replace("2", "1").replace("B", "A").replace("11A", "*")

arr = []
k = 0
for i in s:
    if i == "*":
        k += 1
    else:
        arr.append(k)
        k = 0

print(max(arr))
# 67