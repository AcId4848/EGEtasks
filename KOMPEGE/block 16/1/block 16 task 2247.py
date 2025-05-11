def f(n):
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return f(n - 2) + n - 2
    if n % 2 != 0:
        return f(n + 2) + n + 2


array = []
for n in range(1, 1000):
    try:
        if len(str(f(n))) == 5:
            array.append(f(n))
    except:
        ...

print(len(array))
# 216