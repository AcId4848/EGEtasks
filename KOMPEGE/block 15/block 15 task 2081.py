from itertools import product


def f(x, A, P, Q):
    return (x in A) or (x in P) or (x not in Q)


P = ["11" + "".join(P) for P in product(["0", "1"], repeat=6)]
Q = ["".join(Q) + "0" for Q in product(["0", "1"], repeat=7)]


A = []
for a in product(["0", "1"], repeat=8):
    if all(f("".join(x), "".join(a), P, Q) for x in product(["0", "1"], repeat=8)):
        break
    if "".join(a)[-1] == "0" and "".join(a)[:2] != "11":
        A.append("".join(a))

print(len(A))
# 96
