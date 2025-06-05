def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for x in range(113000000, 114000000+1):
    if x % 2 == 0 and x % 4 != 0:
        t = x // 2
        if int(t ** 0.5) ** 2 == t and prime(int(t ** 0.5)):
            print(x, 2 * int(t ** 0.5))