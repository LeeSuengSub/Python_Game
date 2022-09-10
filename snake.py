from turtle import Turtle, Screen
import time
import random

def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x,rand_y

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font = ("", 15,"bold"))

def game_over():
    game_on = False
    score_pen.goto(0,0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))

screen = Screen()
screen.setup(600,600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0)

# snake 만들기
start_pos = [(0,0), (-20,0), (-40,0)]
snakes = []
score = 0
for pos in start_pos:
    create_snake(pos)

# 먹이
food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

# 점수 표시
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270,250)
score_pen.write(f"점수 : {score}", font = ("", 15,"bold"))

screen.listen()
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())

    snakes[0].forward(20)

    if snakes[0].distance(food) < 15:
        score_update()
        
        food.goto(rand_pos())
        create_snake(snakes[-1].pos())

    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 \
        or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
            game_over()

    for body in snakes[1:]:
        if snakes[0].distance(body)< 10:
            game_over()
