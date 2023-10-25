import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = data[data.state == answer_state]
        turtle.goto(int(state.x), int(state.y))
        turtle.write(answer_state)

