def f(curr, end):
    if curr == end:
        return 1
    elif curr < end:
        return 0
    else:
        return f(curr - 2, end) + f(curr // 2, end)

print(f(38, 16) * f(16, 2))