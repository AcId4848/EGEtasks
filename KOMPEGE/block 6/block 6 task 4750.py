from turtle import *

tracer(0)
r = 50
lt(90)
x = y = 0

for a in range(2):
    x += 6
    y += 2
    goto(x * r, y * r)
    x += 0
    y += -2
    goto(x * r, y * r)
for b in range(3):
    x += 2
    y += -1
    goto(x * r, y * r)
    x += -2
    y += -1
    goto(x * r, y * r)
for c in range(6):
    x += -2
    y += 1
    goto(x * r, y * r)

up()
for x in range(15):
    for y in range(-6, 3):
        goto(x * r, y * r)
        dot(3)

exitonclick()
# 54