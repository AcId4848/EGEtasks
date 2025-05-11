s = open("17_2003.txt")

arr = []
for i in s:
    if int(i) % 3 == 0 and int(i) % 7 != 0 and int(i) % 17 != 0 and int(i) % 19 != 0 and int(i) % 27 != 0:
        arr.append(int(i))

print(len(arr), max(arr))
#445 9738