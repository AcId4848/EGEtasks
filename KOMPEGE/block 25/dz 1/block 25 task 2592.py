def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for x in range(55000000, 60000001):
    t = x
    while t % 2 == 0:
        t //= 2
    if int(t ** 0.25) ** 4 == t and prime(int(t ** 0.25)):
        print(x, t)
