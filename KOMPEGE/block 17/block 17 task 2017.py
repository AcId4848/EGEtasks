s = open("17_2017.txt")

arr = []
for i in s:
    if hex(int(i))[-1] == "b" and int(i) % 7 == 0 and int(i) % 6 != 0 and int(i) % 13 != 0 and int(i) % 19 != 0:
        arr.append(int(i))

print(sum(arr), len(arr))
# 74452 12