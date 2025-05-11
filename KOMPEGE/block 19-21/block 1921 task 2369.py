def f(s1, s2, s3, m):
    if s1 + s2 + s3 >= 73:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 + 3, s2, s3, m - 1), f(s1 + 13, s2, s3, m - 1), f(s1 + 23, s2, s3, m - 1), f(s1, s2 + 3, s3, m - 1),
         f(s1, s2 + 13, s3, m - 1), f(s1, s2 + 23, s3, m - 1), f(s1, s2, s3 + 3, m - 1), f(s1, s2, s3 + 13, m - 1),
         f(s1, s2, s3 + 23, m - 1)]
    return all(h) if m % 2 == 0 else any(h)


print([s for s in range(1, 24) if not f(2, s, 2 * s, 1) and f(2, s, 2 * s, 2)]) # 9
print([s for s in range(1, 24) if not f(2, s, 2 * s, 1) and f(2, s, 2 * s, 3)]) # 8 14
print([s for s in range(1, 24) if not f(2, s, 2 * s, 2) and f(2, s, 2 * s, 4)]) # 10 13