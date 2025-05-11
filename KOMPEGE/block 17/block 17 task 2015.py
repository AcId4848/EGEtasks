s = open("17_2015.txt")

arr = []
for i in s:
    if (i[-2] == "5" or i[-2] == "7") and int(i) % 9 != 0 and int(i) % 11 != 0:
        arr.append(int(i))

print(len(arr), min(arr) + max(arr))
# 337 10802