from turtle import *

tracer(0)
r = 50
lt(90)
x = y = 0
screensize(20000, 20000)
for a in range(5):
    x += 6
    y += 8
    goto(x * r, y * r)
    x += -8
    y += 4
    goto(x * r, y * r)
    x += 2
    y += -12
    goto(x * r, y * r)

up()
for x in range(-2, 7):
    for y in range(13):
        goto(x * r, y * r)
        dot(3)

exitonclick()
# 31