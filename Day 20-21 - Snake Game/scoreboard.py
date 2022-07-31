from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scorekeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.pencolor("white")
        self.penup()
        self.goto(x=0, y=275)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def over_sign(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over.", move=False, align=ALIGNMENT, font=FONT)
