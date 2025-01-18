# TODO-1: Create a snake body
# TODO-2: Move the snake
# TODO-3: Control the snake
# TODO-4: Detect collision with food
# TODO-5: Create a scoreboard
# TODO-6: Detect collision with wall
# TODO-7: Detect collision with tail

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO-1: Create a snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# TODO-3: Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# # Before Move to OOP
# starting_positiosn = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # TODO-2: Move the snake
    # # Before Move to OOP
    # for seg_num in range(len(segments) - 1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segment[0].forward(20)
    snake.move()

    # TODO-4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # TODO-5: Create a scoreboard
        scoreboard.increase_scoreboard()

    # TODO-6: Detect collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    # TODO-7: Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
