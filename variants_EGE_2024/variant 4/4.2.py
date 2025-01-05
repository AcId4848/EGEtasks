from itertools import product, permutations


def f(w, x, y, z):
    return (not (w <= x)) or ((not z) <= (not y)) or z


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, 0, 1, a1), (1, a2, a3, a4), (a5, a6, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p)

# Correct answer: yzxw
# Solved on the first try