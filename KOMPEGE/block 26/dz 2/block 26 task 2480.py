f = open("26_2480.txt")

n = int(f.readline())
a = [0] * 2000001
for i in range(n):
    st, end = map(int, f.readline().split())
    a[st] += 1
    a[end] -= 1


k = 0
st, end = -1, 0
count, length = 0, 0
for i in range(2000001):
    k0 = k
    k += a[i]
    if k > 0 and st == -1:
        st = i
    if k == 0 and k0>0:
        end = i
        count += 1
        length += end - st
        st, end = -1, 0
print(count, length)


