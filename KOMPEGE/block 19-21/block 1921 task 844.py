def f(s, m):
    if 43 <= s <= 72:
        return m % 2 == 0
    elif s > 72:
        return m % 2 != 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1), f(s * 2, m - 1), f(s * 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print([s for s in range(1, 43) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 43) if not f(s, 2) and f(s, 4)])