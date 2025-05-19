f = [int(s) for s in open("17_4622.txt")]
r = [s for s in f if s % 19 == 0 and s > 0]

arr = []
for i in range(len(f)-1):
    srd = [f[i], f[i+1]]
    if (f[i] + f[i+1]) < min(r):
       arr.append(abs(f[i] + f[i+1]))

print(len(arr), max(arr))