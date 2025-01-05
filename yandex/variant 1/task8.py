from itertools import permutations

counter = 0
for i in permutations("AРТЁМ"):
    if (i[0] != "A" or i[-1] != "Ё") and (i[-1] != "A" or i[0] != "Ё"):
        counter += 1
print(counter)