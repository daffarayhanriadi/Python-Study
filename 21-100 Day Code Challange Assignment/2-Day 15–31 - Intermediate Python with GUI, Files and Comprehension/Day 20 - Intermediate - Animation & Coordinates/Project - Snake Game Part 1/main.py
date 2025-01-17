import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO-1: Create a snake body
snake = Snake()

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

screen.exitonclick()
