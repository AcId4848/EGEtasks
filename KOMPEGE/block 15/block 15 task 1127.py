def f(x, A):
    return (A % 7 == 0) and ((240 % x == 0) <= ((A % x != 0) <= (780 % x != 0)))


for A in range(1, 100000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break

# 420
