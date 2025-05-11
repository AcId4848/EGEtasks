def f(s1, s2, m):
    if s1 + s2 >= 59:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1),]
    return all(h) if m % 2 == 0 else any(h)

print([s2 for s2 in range(1, 54) if f(5, s2, 1)]) # 27
print([s2 for s2 in range(1, 54) if not f(5, s2, 1) and f(5, s2, 3)]) # 24 26
print([s2 for s2 in range(1, 54) if not f(5, s2, 2) and f(5, s2, 4)])