# My TODO
# TODO-1: Create 2 paddles
# TODO-2: Create a ball
# TODO-3: Control the left paddle
# TODO-4: Auto move for the right paddle
# TODO-5: Move the ball
# TODO-6: Detect collision with the paddle
# TODO-7: Create a scoreboard for each paddles
# TODO-8: Divide the board to two section

# The Course TODO
# TODO-1: Create the screen
# TODO-2: Create and move a paddle
# TODO-3: Create another paddle
# TODO-4: Create the ball and make it move
# TODO-5: Detect collision with wall and bounce
# TODO-6: Detect collision with paddle
# TODO-7: Detect when paddle misses
# TODo-8: Keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard((100, 200))
l_scoreboard = Scoreboard((-100, 200))

# # Before Move to OOP
# paddle = Turtle(shape="square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
#
#
# def go_up():
#     # global y
#     # y += 20
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
bounce = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Wall
    # if ball.ycor() > 300 or ball.ycor() < -300:
    if abs(ball.ycor()) > 280:
        # Need to bounce
        # while bounce:
        #     time.sleep(0.1)
        #     screen.update()
        #     ball.bounce()
        ball.bounce_y()

    # Detect Collision with Paddle
    is_collision_r_paddle = ball.distance(r_paddle) < 50 and ball.xcor() > 320
    is_collision_l_paddle = ball.distance(l_paddle) < 50 and ball.xcor() < -320

    if is_collision_r_paddle or is_collision_l_paddle:
        ball.bounce_x()
        # ball.increase_speed()

    # Detect when paddle misses
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        l_scoreboard.increase_scoreboard()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.increase_scoreboard()

screen.exitonclick()
