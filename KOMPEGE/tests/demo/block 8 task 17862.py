from itertools import product

count = 0

for i in product("0123456789AB", repeat = 5):
    i = "".join(i)
    if i.count("7") == 1 and i[0] != "0" and i.count("9") + i.count("A") + i.count("B") <= 3:
        count += 1

print(count)