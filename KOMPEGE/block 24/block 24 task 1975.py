s = open("24_1975.txt").readline()

s = s.replace("PP", "P P")

print(max(len(c) for c in s.split()))
# 188