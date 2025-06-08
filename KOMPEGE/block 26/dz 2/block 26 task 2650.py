f = open("26_2650.txt")

L, M, N = map(int, f.readline().split())
a = [0] * (L + 1)
for i in range(N):
    st, l = map(int, f.readline().split())
    a[st] += 1
    a[st+l] -= 1

k = 0
st, end = 0, 0
count, ml = 0, 0
for i in range(L+1):
    k0 = k
    k += a[i]
    if k == 0 and st == 0:
        st = i
    if (k == 1 and k0 == 0) or i == L:
        end = i
        length = end - st
        if length >= M:
            count += 1
            ml = max(ml, length)
        st, end = 0, 0

print(count, ml)
# 577 24426