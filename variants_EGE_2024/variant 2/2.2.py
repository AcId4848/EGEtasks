from itertools import product, permutations


def f(x, y, z, w):
    return (not (y <= x)) or (y == w) or z


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, a2, 1, 1), (a3, a4, 1, a5), (0, 1, a6, 1)]
    if len(set(table)) == len(table):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(p)

# Correct answer: zywx
# Solved on the first try
