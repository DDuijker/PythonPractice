import turtle
import pandas

screen = turtle.Screen()
screen.title("US States game")
background_img = "./blank_states_img.gif"
turtle.addshape(background_img)

turtle.shape(background_img)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
score = 0
game_title = "Guess the state"
guessed_states = []


def write_state(name, x_pos, y_pos):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x=x_pos, y=y_pos)
    text.write(name)


def save_game():
    states_to_learn = []
    for state in all_states:
        if state not in guessed_states:
            states_to_learn.append(state)

    df = pandas.DataFrame(states_to_learn)
    df.to_csv("./states-to-learn.csv")


while score < 50:
    # Enter a new answer (with a loop)
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?")

    # Check if the user typed in "Exit" clicked "Cancel"
    if answer_state == "Exit" or answer_state is None:
        save_game()
        break
    else:

        answer_state = answer_state.title()

        if answer_state in all_states:
            # Search for the row where the name of the state is the same one you guessed
            score += 1
            guessed_states.append(answer_state)
            state_row = data[data.state == answer_state]
            x_pos = int(state_row.x.iat[0])
            y_pos = int(state_row.y.iat[0])
            write_state(answer_state, x_pos=x_pos, y_pos=y_pos)
            game_title = f"{score}/50 States Guessed Correctly"
