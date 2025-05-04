from itertools import permutations


def f(a, b, c, d):
    return ((a and b) == (not c)) and (b <= d)


table = [(1, 0, 0, 0), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0)]
if len(table) == len(set(table)):
    for p in permutations("abcd"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]:
            print(p)

# cadb