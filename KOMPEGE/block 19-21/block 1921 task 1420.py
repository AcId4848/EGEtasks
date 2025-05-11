def f(s1, s2, m):
    if s1 * s2 >= 63:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1)]
    return all(h) if m % 2 == 0 else any(h)


print([s for s in range(1, 32) if not f(2, s, 1) and f(2, s, 2)]) # 15
print([s for s in range(1, 32) if not f(2, s, 1) and f(2, s, 3)]) # 7 14
print([s for s in range(1, 32) if not f(2, s, 2) and f(2, s, 4)]) # 13