def f(n):
    if n <= 1:
        return n
    if n > 1 and n % 3 == 0:
        return n + f(n / 3)
    if n > 1 and n % 3 != 0:
        return n + f(n + 3)


for n in range(1, 100):
    try:
        if f(n) > 100:
            print(n)
    except:
        ...

# 81