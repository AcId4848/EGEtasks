f = open('290F15.txt')
k = int(f.readline())
n = int(f.readline())
a = [[int(y) for y in x.split()] for x in f]
a.sort()
lockers = [0] * k
count = 0
last = 0
lasttime = 0
for i in a:
    locker = -1
    for j in range(0, k):
        if lockers[j] < i[0]:
            locker = j
            break
    if locker != -1:
        if i[0] > lasttime:
            last = locker + 1
            lasttime = i[0]
        count += 1
        lockers[locker] = i[1]
print(count, last)