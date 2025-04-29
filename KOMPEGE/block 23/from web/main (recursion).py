def f(curr, end):
    if curr > end:
        return 0
    # if curr > end or curr == 4:
    #     return 0
    if curr == end:
        return 1
    if curr < end:
        return f(curr + 1, end) + f(curr * 2, end)

print(f(2, 10))

# print(f(2, 8)*f(8, 20))

# 7

