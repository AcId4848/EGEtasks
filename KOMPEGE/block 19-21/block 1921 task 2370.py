def f(s, m):
    if s >= 2163:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 1, m - 1), f(s * 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print([s for s in range(1, 2163) if not f(s, 1) and f(s, 2)]) # 720
print([s for s in range(1, 2163) if not f(s, 1) and f(s, 3)]) # 240 719
print([s for s in range(1, 2163) if not f(s, 2) and f(s, 4)]) # 718