array = []
for n in range(1, 10000):
    R = [n // 3, n - 1][0 if n % 3 == 0 else 1]
    R = [R // 5, R - 1][0 if R % 5 == 0 else 1]
    R = [R // 11, R - 1][0 if R % 11 == 0 else 1]
    if R == 8:
        array.append(n)

print(len(array))
# 4