from turtle import *

tracer(0)
r = 25
lt(90)
x = y = 0
for a in range(3):
    x += -3
    y += -4
    goto(x * r, y * r)
    x += -12
    y += -5
    goto(x * r, y * r)
    x += 0
    y += 1
    goto(x * r, y * r)
    x += 15
    y += 8
    goto(x * r, y * r)

up()
for x in range(-15, 1):
    for y in range(-9, 1):
        goto(x * r, y * r)
        dot(3)

exitonclick()