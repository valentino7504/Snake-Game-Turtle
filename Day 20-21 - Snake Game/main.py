from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scorekeeper

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Frenzy")
screen.tracer(0)
scorekeeper = Scorekeeper()
valentino = Snake()
food = Food()
screen.listen()
screen.onkey(fun=valentino.up, key="Up")
screen.onkey(fun=valentino.up, key="w")
screen.onkey(fun=valentino.left, key="Left")
screen.onkey(fun=valentino.left, key="a")
screen.onkey(fun=valentino.down, key="Down")
screen.onkey(fun=valentino.down, key="s")
screen.onkey(fun=valentino.right, key="Right")
screen.onkey(fun=valentino.right, key="d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    valentino.move()
    if valentino.head.distance(food) < 15:
        food.refresh()
        valentino.extend()
        scorekeeper.increase_score()

    # Detect collision with wall:
    if valentino.head.xcor() > 285 or valentino.head.ycor() > 299 \
            or valentino.head.ycor() < -285 or valentino.head.xcor() < -299:
        game_is_on = False
        scorekeeper.over_sign()

    # Collision with tail
    for segment in valentino.segments[1:]:
        if valentino.head.distance(segment) < 10:
            game_is_on = False
            scorekeeper.over_sign()
screen.exitonclick()
