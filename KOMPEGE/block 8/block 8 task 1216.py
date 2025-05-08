from itertools import product


array = []
for i in product("01234", repeat=6):
    i = "".join(i)
    if i[0] != "1" and i[0] != "0" and i[-1] != "3" and i[-1] != "4":
        array.append(i)
        print(i)

print(len(array))
# 5625