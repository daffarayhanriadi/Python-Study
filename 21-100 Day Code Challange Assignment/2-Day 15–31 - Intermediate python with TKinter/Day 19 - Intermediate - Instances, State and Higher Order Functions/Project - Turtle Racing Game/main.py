import random
import turtle as t

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = [-100, -50, 0, 50, 100, 150]
turtles = []

for idx in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y[idx])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        rand_forward = random.randint(0, 10)
        turtle.forward(rand_forward)

screen.exitonclick()
