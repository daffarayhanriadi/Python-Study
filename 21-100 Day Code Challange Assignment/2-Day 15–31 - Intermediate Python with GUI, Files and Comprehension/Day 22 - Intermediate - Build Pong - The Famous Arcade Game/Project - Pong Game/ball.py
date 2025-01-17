from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move  # 10
        new_y = self.ycor() + self.y_move  # 10
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # new_x = self.xcor() + 10
        # new_y = self.ycor() - 10
        # self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase the ball's speed

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    # def increase_speed(self):
    #     self.x_move *= 1.1
    #     self.y_move *= 1.1
