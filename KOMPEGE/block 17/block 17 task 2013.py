s = open("17_2013.txt")

arr = []
for i in s:
    if (i[-2] == "2" or i[-2] == "7") and int(i) % 3 == 0 and int(i) % 11 == 0:
        arr.append(int(i))

print(len(arr), min(arr))
# 13 1287