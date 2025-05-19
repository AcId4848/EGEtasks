for i in range(550000, 1000000):
    de = [d for d in range(2, i-1) if i % d == 0]
    if len(de) == 0:
        de = [0]
    f = sum(de) // len(de)
    if f % 31 == 13:
        print(i, f)

# 550032 28285
# 550040 49117
# 550046 28905
# 550050 19419
# 550066 35725