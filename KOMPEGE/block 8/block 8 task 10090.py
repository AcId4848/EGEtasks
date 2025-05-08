from itertools import permutations

a = []
for x in permutations("0234567", 5):
    p = "".join(x)
    if p[0] != "0":
        p = p.replace("0", "Ч").replace("2", "Ч").replace("4", "Ч").replace("6", "Ч")
        p = p.replace("3", "Н").replace("5", "Н").replace("7", "Н")
        if "НН" not in p and "ЧЧ" not in p:
            print(x, p)
            a.append(p)

print(len(a))