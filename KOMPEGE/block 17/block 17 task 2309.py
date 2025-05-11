s = [int(f) for f in open("17_2309.txt")]

arr_11 = []
arr_17 = []

for i in s:
    if i % 11 == 0:
        arr_11.append(i)
    if i % 17 == 0:
        arr_17.append(i)

# print(len(arr_17))
print(len(arr_11), min(arr_11))
# 70 363