def f(a, b, m):
    if a + b >= 45:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, b, m - 1), f(a * 3, b, m - 1), f(a, b + 1, m - 1), f(a, b * 3, m - 1)]
    return any(h) if (m-1) % 2 == 0 else all(h) # меняем в 19ой all на any


print("19)", [s for s in range(1, 41) if f(4, s, 2)])
print()