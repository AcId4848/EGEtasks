from itertools import product, permutations


def f(w, x, y, z):
    return x and (y <= z) and ((not z) <= ((not z) == w))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(a1, a2, 0, 0), (a3, 0, 0, a4), (1, a5, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [1, 1, 0]:
                print(*p)

# Correct answer: xzyw
# Solved on the first try