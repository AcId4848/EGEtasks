from itertools import permutations

array = []
for a in permutations("ИГРОК"):
    if a[0] != "К" and "РОК" not in "".join(a):
        array.append(a)

print(array)
print(len(array))
# 90