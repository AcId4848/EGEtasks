from itertools import permutations

for n in range(100, 1000):
    n = str(n)
    a = [int("".join(p)) for p in permutations(n, 2) if p[0] != "0"]
    if max(a) - min(a) == 5:
        print(n)
        break

# 505