from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-280, 240)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_scoreboard(self):
        self.level += 1
        self.update_scoreboard()
