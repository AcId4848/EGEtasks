def f(s1, s2, m):
    if s1 + s2 >= 68:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 + s2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 + s1, m - 1)]
    return all(h) if m % 2 == 0 else any(h)


print([s for s in range(1, 60) if not f(8, s, 1) and f(8, s, 2)]) # 18 при any
print([s for s in range(1, 60) if not f(8, s, 1) and f(8, s, 3)]) # 17 29
print([s for s in range(1, 60) if not f(8, s, 2) and f(8, s, 4)]) # 28