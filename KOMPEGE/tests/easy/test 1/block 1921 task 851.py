def f(s1, s2, m):
    if s1 + s2 >= 45:
        return 1
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m-1), f(s1 * 3, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print([s for s in range(1, 41) if f(4, s, 2) and not f(4, s, 1)])
print([s for s in range(1, 41) if not f(4, s, 1) and f(4, s, 3)])
print([s for s in range(1, 41)])
