from turtle import *
r = 40
lt(90)
tracer(0)
screensize(20000, 20000)
x = y = 0
goto(x, y)
for a in range(10):
    x += 3
    y += 6
    goto(x * r, y * r)
    x += 7
    y += -2
    goto(x * r, y * r)
    x += -10
    y += -4
    goto(x * r, y * r)

up()
for x in range(10):
    for y in range(7):
        goto(x * r, y * r)
        dot(3)

exitonclick()
# 22