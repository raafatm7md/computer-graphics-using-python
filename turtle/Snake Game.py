from turtle import *
from time import *
from random import *

score = 0
highest = 0
speed = 0.1
title("Snake")
bgcolor('black')
setup(700, 700)
tracer(0)

ts1 = Turtle()
ts2 = Turtle()
ts1.color("white")
ts1.penup()
ts1.hideturtle()
ts1.goto(270, 310)
ts1.write("Score : 0", align="center", font=("Arial", 20, "bold"))
ts2.color("white")
ts2.penup()
ts2.hideturtle()
ts2.goto(220, -340)
ts2.write("Highest score : 0", align="center", font=("Arial", 20, "bold"))

game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()

snake = Turtle()
snake.speed(0)
snake.shape("square")
snake.color("red")
snake.penup()
Dir = "None"

food = Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(150, 0)
body = []


def up():
    global Dir
    if Dir != "down":
        Dir = "up"


def down():
    global Dir
    if Dir != "up":
        Dir = "down"


def left():
    global Dir
    if Dir != "right":
        Dir = "left"


def right():
    global Dir
    if Dir != "left":
        Dir = "right"

listen()
onkeypress(up, "Up")
onkeypress(up, "w")
onkeypress(down, "Down")
onkeypress(down, "s")
onkeypress(left, "Left")
onkeypress(left, "a")
onkeypress(right, "Right")
onkeypress(right, "d")


def move():
    global Dir
    if Dir == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if Dir == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if Dir == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if Dir == "right":
        x = snake.xcor()
        snake.setx(x + 20)


while True:
    update()
    if snake.xcor() > 340 or snake.xcor() < -340 or snake.ycor() > 340 or snake.ycor() < -340:
        sleep(1)
        snake.goto(0, 0)
        Dir = "None"
        for B in body:
            B.goto(999, 999)
        body.clear()
        score = 0
        speed = 0.1

        game_over.write("Game Over!", align='center', font=("Arial", 50, "bold"))
        sleep(0.5)
        game_over.clear()

        ts1.clear()
        ts2.clear()
        ts1.write(f"Score : {score}", align="center", font=("Arial", 20, "bold"))
        ts2.write(f"Highest score : {highest}", align="center", font=("Arial", 20, "bold"))

    if snake.distance(food) < 20:
        x = randint(-330, 330)
        y = randint(-330, 330)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        food.color(r, g, b)
        food.goto(x, y)

        new_body = Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("red")
        new_body.penup()
        body.append(new_body)

        speed -= 0.001
        score += 1

        if score > highest:
            highest = score
        ts1.clear()
        ts1.write(f"Score : {score}", align="center", font=("Arial", 20, "bold"))

    for index in range(len(body) - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    move()

    for B in body:
        if B.distance(snake) < 20:
            sleep(1)
            snake.goto(0, 0)
            Dir = "None"

            for B in body:
                B.goto(1000, 1000)
            body.clear()

            game_over.write("Game Over!", align='center', font=("Arial", 50, "bold"))
            sleep(0.5)
            game_over.clear()

            score = 0
            speed = 0.1

            ts1.clear()
            ts2.clear()
            ts1.write(f"Score : {score}", align="center", font=("Arial", 20, "bold"))
            ts2.write(f"Highest score : {highest}", align="center", font=("Arial", 20, "bold"))
    sleep(speed)
