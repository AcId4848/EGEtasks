def f(s, m):
    if s == 0:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s - i, m - 1) for i in range(1, s // 2 + 1)]
    return all(h) if m % 2 == 0 else any(h)

print([s for s in range(1, 100) if f(s, 6)])