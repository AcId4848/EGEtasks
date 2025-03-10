from itertools import product, permutations


def f(w, x, y, z):
    return (x or (not y)) and (not (y == z)) and w


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    table = [(0, 1, a1, 0), (a2, 1, 1, 0), (1, a3, 0, a4)]
    if len(table) == len(set(table)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
                print(*p)