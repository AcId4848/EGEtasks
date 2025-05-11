from turtle import *
tracer(0)
lt(90)
r = 20
rt(270)
for a in range(8):
    fd(10 * r)
    rt(45)
    fd(10 * r)
    rt(135)
for b in range(4):
    fd(4 * r)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(3)

exitonclick()
# 98