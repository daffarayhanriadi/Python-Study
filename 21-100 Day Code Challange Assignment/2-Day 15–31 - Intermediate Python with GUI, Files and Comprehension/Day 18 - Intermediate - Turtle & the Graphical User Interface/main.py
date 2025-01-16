import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
# tim.shape("turtle")
tim.color("red")

"""
Challange 1: Draw a Square
"""
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

"""
Challange 2: Draw a Dashed Line
"""
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

"""
Challange 3: Draw Different Shapes
triangle, square, pentagon, hexagon, octagon, nonagon, decagon
"""

# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_sides_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_sides_n)

## ALTERNATIVE SOLUTION
# side_num = [3, 4, 5, 6, 7, 8, 9, 10]

# for side in side_num:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     for _ in range(side):
#         tim.color(r, g, b)
#         tim.forward(100)
#         tim.right(360 / side)


"""
Challange 4: Draw a Random Walk
"""
# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

## ALTERNATIVE SOLUTION
# tim.speed(10)

# for _ in range(100):
#     tim.color(random.choice(colours))
#     tim.forward(100)
#     tim.right(random.randrange(0, 270, 90)) # Degrees


"""---------------------------Learn Tuples----------------------------------"""
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b) # Tuples
#     return random_color


# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

"""
Challange 5: Draw a Spiograph
"""

tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spiograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spiograph(5)


# # ALTERNATIVE SOLUTION
# slope = 5
# while True:
#     tim.color(random_color())
#     tim.circle(120)
#     tim.left(slope)

screen = t.Screen()
screen.exitonclick()
