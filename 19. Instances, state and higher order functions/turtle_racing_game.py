from turtle import Turtle, Screen
import random
import turtle as t

t.title("Turtle Racing Betting Game")

# Set up pen for start and finish line
pen = Turtle("blank")
# Set up screen
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# Define constants
COLORS = ["red", "orange", "gold", "green", "blue", "purple"]
HEIGHT = 400
WIDTH = 500
# Calculate dynamic height based on available height
available_height = HEIGHT * 0.5
margin = (HEIGHT - available_height) / 2
height_between_turtles = available_height / len(COLORS)
start_y_position = -200 + margin
start_x_position = -225

all_turtles = []


def draw_finish_line():
    global pen
    pen.color("red")
    pen.penup()
    # Go from up to down
    pen.goto(x=230, y=200)
    pen.pendown()
    pen.setheading(270)
    pen.forward(400)
    pen.penup()


def draw_start_line():
    global pen
    pen.color("blue")
    pen.penup()
    # Go from up to down
    pen.goto(x=-225, y=200)
    pen.pendown()
    pen.setheading(270)
    pen.forward(400)
    pen.penup()


# This is placed before the turtles are lined up, because I want the turtles ON the line, not under.
draw_start_line()

# For every color in color list, make a turtle and put it at the right y position
for index in range(len(COLORS)):
    new_turtle = Turtle("turtle")
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.color(COLORS[index])
    start_y_position += height_between_turtles
    new_turtle.goto(x=start_x_position, y=start_y_position)
    # Add to the list
    all_turtles.append(new_turtle)

# Make race not start prematurely
if user_bet:
    draw_finish_line()
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")
            is_race_on = False
        # Generate random distance ( between 0 and 10, including 10)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
