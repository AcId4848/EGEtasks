from itertools import product, permutations


def f(w, x, y, z):
    return (not (x <= y)) or (x == z) or w


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    table = [(1, 0, a1, 1), (a2, a3, 1, 1), (a4, a5, 1, a6)]
    if len(table) == len(set(table)):
        for p in permutations("wxyz"):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p)

# Correct answer: xwzy
# Solved on the first try
