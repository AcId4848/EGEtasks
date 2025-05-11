from turtle import *
tracer(0)
r = 30
lt(90)
screensize(20000, 20000)
lt(255)
for a in range(3):
    lt(30)
    for b in range(4):
        fd(10*r)
        lt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r)
        dot(3)
update()
exitonclick()
# 56