array = []
for N in range(1, 100):
    R = bin(N)[2:]
    R += str(sum([int(i) for i in R]) % 2)
    R += str(sum([int(i) for i in R]) % 2)
    R = int(R, 2)
    if R < 80:
        array.append(R)

print(len(array))
# 19
