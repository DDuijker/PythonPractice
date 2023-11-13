from turtle import Turtle, Screen
from paddle import Paddle
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

right_paddle = Paddle(x_position=350)
left_paddle = Paddle(x_position=-350)
KEYBINDINGS = [['w', 's'], ['Up', 'Down']]
screen.listen()


# For loop to enable keybinds
def register_keybindings(paddle, keys):
    screen.onkey(paddle.up, keys[0])
    screen.onkey(paddle.down, keys[1])


register_keybindings(left_paddle, KEYBINDINGS[0])
register_keybindings(right_paddle, KEYBINDINGS[1])

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
