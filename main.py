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

correct_guesses = []
game_is_on = True
while game_is_on:
    data = pandas.read_csv("50_states.csv")
    states = data["state"].to_list()

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} States Correct", prompt="What's \
    another state's name?").title()

    if answer_state in states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = data[data.state == answer_state]
        turtle.goto(int(state.x), int(state.y))
        turtle.write(answer_state)

    if len(correct_guesses) == 50:
        game_is_on = False

screen.exitonclick()
