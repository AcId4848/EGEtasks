for n in range(1, 1000):
    n = str(n)
    a = sum([int(i) for i in n if int(i) % 2 == 0])
    b = sum([int(j) for j in n[::-2] if len(n) != 1])
    R = abs(a - b)
    if R == 9:
        print(n)
        break

# 19