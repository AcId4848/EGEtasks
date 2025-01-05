from itertools import product, permutations


def f(w, x, y, z):
    return (not (x <= y)) or ((not w) <= (not z)) or w


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(a1, a2, 1, a3), (1, 1, a4, a5), (a6, 1, 1, 0)]
    if len(set(table)) == len(table):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(p)

# Correct answer: xyzw
# Solved on the first try