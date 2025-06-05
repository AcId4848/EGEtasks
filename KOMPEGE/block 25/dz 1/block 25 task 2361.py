def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and i % 10 == 7:
            d |= {i}
        if x % i == 0 and x // i % 10 == 7:
            d |= {x // i}
    return sorted(d)


for x in range(550000, 550300):
    d = div(x)
    if len(d) == 3:
        print(x, d[-1])

# 550014 275007
# 550017 1567
# 550032 34377
# 550035 110007
# 550037 9017