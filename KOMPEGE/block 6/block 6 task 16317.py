from turtle import *

tracer(0)
lt(90)
r = 20
pendown()
screensize(20000, 20000)
for a in range(2):
    fd(21*r)
    rt(90)
    fd(27*r)
    rt(90)
up()
fd(9*r)
rt(90)
fd(10*r)
lt(90)
down()
for b in range(2):
    fd(86*r)
    rt(90)
    fd(47*r)
    rt(90)

up()
for x in range(28):
    for y in range(22):
        goto(x*r, y*r)
        dot(3)
update()
exitonclick()
# 234