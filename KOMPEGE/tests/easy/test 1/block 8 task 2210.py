from itertools import permutations


a = []
for i in permutations("КРОВЬ"):
    i = "".join(i)
    if i[0] != "Ь" and "ЬО" not in i and "ОЬ" not in i:
        a.append(i)

print(len(a), a)