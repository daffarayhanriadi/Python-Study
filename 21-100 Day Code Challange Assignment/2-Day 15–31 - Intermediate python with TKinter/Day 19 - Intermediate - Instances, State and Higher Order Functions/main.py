import turtle as t

tim = t.Turtle()
screen = t.Screen()


# def move_forward():
#     tim.forward(10)


# screen.listen()
# screen.onkey(key="space", fun=move_forward)
# screen.exitonclick()

"""
Functions as Inputs
"""


# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# def calculator(n1, n2, func):
#     return func(n1, n2)


# result = calculator(2, 3, add)
# print(result)


"""
Challenge: Make an Etch-A-Sketch App
"""


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


# counter_clockwise
def turn_left():
    tim.left(10)

    # ALTERNATIVE SOLUTION
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)

# clockwise
def turn_right():
    tim.right(10)

    # ALTERNATIVE SOLUTION
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(forwards, "w")
screen.onkey(backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")
screen.listen()
screen.exitonclick()
