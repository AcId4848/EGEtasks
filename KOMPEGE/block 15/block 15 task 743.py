def f(x, A):
    return ((x not in [1, 3, 5, 7, 9, 11]) or (x not in [3, 6, 9, 12])) or (x in A)



A = [3, 9]
print(all(f(x, A) for x in range(100)))
# 12