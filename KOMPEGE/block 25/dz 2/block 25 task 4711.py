from fnmatch import fnmatch
for x in range(0, 10 ** 10, 2023):
    if fnmatch(str(x), "1?2139*4"):
        print(x, x // 2023)

# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048
