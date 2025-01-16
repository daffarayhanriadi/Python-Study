import random
import turtle as t

from colors import color_list

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

## ALTERNATIVE SOLUTION
# x = 0
# y = -200
# tim.setpos(x, y)

# for _ in range(10):
#     for _ in range(10):
#         tim.forward(50)
#         tim.dot(20, random.choice(color_list))
#     y += 50
#     tim.setpos(x, y)

screen = t.Screen()
screen.exitonclick()
