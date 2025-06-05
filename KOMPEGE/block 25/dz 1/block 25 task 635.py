def prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


for x in range(102, 112):
    if prime(x):
        print(x ** 4, x ** 3)