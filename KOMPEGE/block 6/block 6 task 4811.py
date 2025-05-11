from turtle import *

tracer(0)
r = 25
lt(90)
x = y = 0

for a in range(5):
    x += 5
    y += 4
    goto(x * r, y * r)
    x += 4
    y += -4
    goto(x * r, y * r)
    x += -7
    y += -2
    goto(x * r, y * r)
    x += -2
    y += 2
    goto(x * r, y * r)

up()
for x in range(10):
    for y in range(-2, 5):
        goto(x * r, y * r)
        dot(3)

exitonclick()
# 27