from itertools import permutations

def f(w, x, y, z):
    return w or (x <= y) and ((not z) <= x)


table = ([0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1])
for p in permutations("wxyz"):
    if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
        print(p)