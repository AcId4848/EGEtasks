array = []

for N in range(1000):
    R = bin(N)[2:]
    R = ["1", "11"][N%2] + R + ["0", "11"][N%2]
    R = int(R, 2)
    if R > 52:
        array.append(R)

print(min(array))
# 56