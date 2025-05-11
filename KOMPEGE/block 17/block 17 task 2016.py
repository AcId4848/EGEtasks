s = open("17_2016.txt")

arr = []
for i in s:
    if int(i) % 13 == 7 and int(i) % 7 != 0 and int(i) % 11 != 0:
        arr.append(int(i))

print(max(arr) - min(arr), len(arr))
