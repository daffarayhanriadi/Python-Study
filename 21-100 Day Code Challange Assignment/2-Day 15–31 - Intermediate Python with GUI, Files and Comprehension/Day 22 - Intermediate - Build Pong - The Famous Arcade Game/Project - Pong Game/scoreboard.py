from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("JetBrainsMono Nerd Font", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=self.score, move=False, align=ALLIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
