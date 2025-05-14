s = open("24_1428.txt").readline()

s = s.replace("XY", "X Y").replace("XZ", "X Z")

print(max(len(c) for c in s.split()))
# 25