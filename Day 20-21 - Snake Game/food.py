from turtle import Turtle
import random

LIST_OF_COLORS = ["red", "yellow", "orange", "pink", "skyblue", "white smoke", "lightgreen", "turquoise"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(LIST_OF_COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(LIST_OF_COLORS))
        random_x = random.randint(-275, 280)
        random_y = random.randint(-280, 275)
        self.goto(random_x, random_y)
