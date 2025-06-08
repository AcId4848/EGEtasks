def f(s, m):
    if s <= 19:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)


print([s for s in range(20, 1000) if not f(s, 1) and f(s, 2)])
print([s for s in range(20, 1000) if not f(s, 1) and f(s, 3)])
print([s for s in range(20, 1000) if not f(s, 2) and f(s, 4)])