a = [x for x in open("17.txt")]
ans = []

counter = 0
for i in range(len(a) - 2):
    max
    if (a[i][2:] == "42" and a[i+1][2:] == "42") or (a[i+2][2:] == "42" and a[i+1][2:] == "42") or (a[i][2:] == "42" and a[i+2][2:] == "42") and \
            (len(a[i] + a[i+1]) == 8 or len(a[i] + a[i+2]) == 8 or len(a[i+1] + a[i+2]) == 8):
        if int(a[i]) + int(a[i+1]) + int(a[i+2]) > max(int(a[i]), int(a[i]), int(a[i])):
            counter += 1
            ans.append(int(a[i]) + int(a[i+1]) + int(a[i+2]))

print(counter, max(ans))