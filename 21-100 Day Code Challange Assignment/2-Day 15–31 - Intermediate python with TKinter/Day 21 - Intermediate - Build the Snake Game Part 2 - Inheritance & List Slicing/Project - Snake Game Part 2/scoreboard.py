from turtle import Turtle

ALIGNMENT = "center"
FONT = ("JetBrainsMono Nerd Font", 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME_OVER", move=False, align=ALIGNMENT, font=FONT)
