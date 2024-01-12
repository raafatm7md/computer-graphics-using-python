from turtle import *


def rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


title("Rose")
speed(0)
pensize(5)
bgcolor("black")
hue = 0.0
n = int(numinput("Rose", "Enter the number of petals: "))
for i in range(0, 200, 4):
    col = rgb(hue, 1, 1)
    pencolor(col)
    hue += 0.02
    for x in range(int(n)):
        for _ in range(2):
            circle(i, 100)
            lt(80)
        rt((360/n))

exitonclick()
