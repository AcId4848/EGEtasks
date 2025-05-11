from turtle import *

r = 25
tracer(0)
x = y = 0
x += -7
y += -1
goto(x * r, y * r)
dot(3)

for N in range(1):
    x += 15
    y += 22
    goto(x, y)
    dot(3)

x += 23
y += -32
goto(x, y)
dot(3)

print(pos())


exitonclick()