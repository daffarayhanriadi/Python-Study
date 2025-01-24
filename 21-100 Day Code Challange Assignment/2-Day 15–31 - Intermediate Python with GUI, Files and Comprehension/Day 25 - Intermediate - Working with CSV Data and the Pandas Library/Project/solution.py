# TODO-1: Convert the guess to Title case
# TODO-2: Check if the guess is among the 50 states
# TODO-3: Write correct guesses onto the map
# TODO-4: Use a loop to allow the user to keep guessing
# TODO-5: Record the correct guesses in a list
# TODO-6: Keep track of the score

import turtle

import pandas

IMAGE = "blank_states.gif"
FILE = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. State Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv(FILE)
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_state)}/50 State Correct",
        prompt="What's another state's name?",
    ).title()  # type: ignore

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # Best way
        t.goto(state_data.x.item(), state_data.y.item())  # type: ignore
        t.write(answer_state)
        # Alternative way
        # t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())

# screen.exitonclick()
