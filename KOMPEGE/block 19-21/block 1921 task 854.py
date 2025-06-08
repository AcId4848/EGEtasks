def f(s, m):
    if s < 10:
        return m % 2 == 0
    if m == 0:
        return 0
    if s % 2 == 0:
        h = [f(s - 1, m - 1), f(s - 2, m - 1), f(s - 3, m - 1), f(s - 4, m - 1), f(s - 5, m - 1), f(s // 2, m - 1)]
    elif s % 2 != 0:
        h = [f(s - 1, m - 1), f(s - 2, m - 1), f(s - 3, m - 1), f(s - 4, m - 1), f(s - 5, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print([s for s in range(11, 70) if f(s, 2)])
print([s for s in range(11, 70) if not f(s, 1) and f(s, 3)])
print([s for s in range(11, 70) if not f(s, 2) and f(s, 4)])