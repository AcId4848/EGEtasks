a = [0] * 100
a[2] = 1
for i in range(2, 10):
    if i + 1 <= 10:
        a[i+1] += a[i]
    if 2 * i <= 10:
        a[i*2] += a[i]
print(a[10])