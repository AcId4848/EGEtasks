from itertools import product, permutations


def f(x, y, z, w):
    return (((not x) and y) == z) and w


for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product([0, 1], repeat=10):
    table = [(a1, 0, a2, a3), (a4, a5, a6, 0), (0, 0, a7, a8), (0, 0, a9, a10)]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
                print(*p)