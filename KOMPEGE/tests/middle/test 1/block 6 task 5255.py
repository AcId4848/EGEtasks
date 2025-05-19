from turtle import *

tracer(0)

x = y = 0
for i in range(8):
    x += 30
    y += 10
    goto(x, y)
    x += 50
    y += -30
    goto(x, y)
    x += -40
    y += 50
    goto(x, y)
    print(i)

print((pos()[0] ** 2 + pos()[1] ** 2) ** 0.5)
# 400