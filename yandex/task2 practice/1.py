from itertools import product, permutations

def f(w, x, y, z):
    return (not (w <= x)) or (y <= z) or (not y)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, 0, a2, a3), (a4, 1, 0, a5), (a6, a7, 1, 0)]
    if len(set(table)) == len(table):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(p)
