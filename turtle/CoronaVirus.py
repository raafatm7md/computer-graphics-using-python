from turtle import *


def corona(length, depth):
    left(120)
    fd(length)
    if depth > 1:
        corona(length / 3, depth - 1)
    bk(length)
    right(60)
    fd(length)
    if depth > 1:
        corona(length / 3, depth - 1)
    bk(length)
    right(60)
    fd(length)
    if depth > 1:
        corona(length / 3, depth - 1)
    bk(length)
    right(60)
    fd(length)
    if depth > 1:
        corona(length / 3, depth - 1)
    bk(length)
    right(60)
    fd(length)
    if depth > 1:
        corona(length / 3, depth - 1)
    bk(length)
    right(60)
    fd(length)
    if depth == 3:
        corona(length / 3, depth - 1)
    bk(length)
    right(180)


title("CoronaVirus")
bgcolor("black")
color("green", "green")
speed(0)
hideturtle()
goto(0, -75)
begin_fill()
circle(75)
end_fill()
goto(0, 0)
pensize(15)
corona(100, 3)

exitonclick()
