from turtle import *


def stars():
    for _ in range(5):
        turtle.fd(10)
        turtle.right(144)


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


def draw_one_color_arc(x, y, ri, pen_width, colour):
    turtle.up()
    turtle.goto(x + ri, y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pen_width)
    turtle.pencolor(colour)
    turtle.circle(ri, 180)


turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
bgcolor('light blue')
title('Rainbow')
num_colors = 49

radius = 350
width = 20*7/num_colors
hue = 0

turtle.color('red', 'yellow')
turtle.up()
turtle.goto(-350, 200)
turtle.down()
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if turtle.pos()[0] <= -349.9 and turtle.pos()[1] < 210:
        break
turtle.end_fill()

for _ in range(num_colors):
    (r, g, b) = rgb(hue, 1, 1)
    draw_one_color_arc(0, -130, radius, width, (r, g, b))
    radius -= (width-1)
    hue += 0.9/num_colors


turtle.up()
turtle.speed(10)
turtle.goto(-800, -130)
turtle.down()
turtle.setheading(0)
turtle.color("Blue", "Blue")
turtle.pendown()
turtle.begin_fill()
turtle.forward(1500)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(1500)
turtle.end_fill()

turtle.up()
turtle.goto(-400, -180)
turtle.down()
turtle.pencolor('white')
turtle.speed(0)
for i in range(7):
    turtle.sety(-180)
    turtle.setheading(45)
    turtle.pendown()
    turtle.circle(-100, extent=100, steps=100)
turtle.up()
turtle.goto(-400, -230)
turtle.down()
for i in range(7):
    turtle.sety(-230)
    turtle.setheading(45)
    turtle.pendown()
    turtle.circle(-100, extent=100, steps=100)
turtle.up()
turtle.goto(-400, -280)
turtle.down()
for i in range(7):
    turtle.sety(-280)
    turtle.setheading(45)
    turtle.pendown()
    turtle.circle(-100, extent=100, steps=100)

exitonclick()
