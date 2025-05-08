from itertools import product


array = []
for p in product("AB123", repeat = 8):
    p = "".join(p)
    if p.count("A") + p.count("B") == 2:
        array.append(p)

print(len(array))
# 81648