import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. State Game")
image = "blank_states.gif"
screen.addshape(image)
t.shape(image)

writer = t.Turtle()
writer.penup()
writer.hideturtle()

score = 0
is_not_over = True
correct_answer = []
all_missing_states = []

df = pd.read_csv("50_states.csv")
all_states = []

for state in df.state:
    all_states.append(state)

while is_not_over:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title() # type: ignore (just for hide the typechecking)


    for state in df.state:
        if answer_state == state:
            a_state = df[df.state == answer_state]
            writer.goto(a_state.x[a_state.index[0]], a_state.y[a_state.index[0]]) # type: ignore (just for hide the typechecking)
            writer.write(answer_state)
            correct_answer.append(answer_state)
            score += 1
    
    if answer_state == "Exit":
        for state in all_states:
            if state not in correct_answer:
                all_missing_states.append(state)
        missing_states = pd.DataFrame({
            "State": all_missing_states
        })
        missing_states.to_csv("states_to_learn_2.csv")
        is_not_over = False

# # To get the x & y coordinate
# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# t.onscreenclick(get_mouse_click_coor)

# t.mainloop()
# screen.exitonclick()