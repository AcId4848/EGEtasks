from itertools import permutations

arr = []
for n in range(300, 400):
    n = str(n)
    a = [int("".join(p)) for p in permutations(n, 2) if p[0] != "0"]
    if max(a) - min(a) == 20:
       arr.append(n)

print(len(arr))
# 12