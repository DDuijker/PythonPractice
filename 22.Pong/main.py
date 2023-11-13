from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
KEYBINDINGS = [['w', 's'], ['Up', 'Down']]
screen.listen()

right_paddle = Paddle(x_position=350)
left_paddle = Paddle(x_position=-350)
ball = Ball()
scoreboard = Scoreboard()


# For loop to enable keybinds
def register_keybindings(paddle, keys):
    screen.onkey(paddle.up, keys[0])
    screen.onkey(paddle.down, keys[1])


register_keybindings(left_paddle, KEYBINDINGS[0])
register_keybindings(right_paddle, KEYBINDINGS[1])

game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.moving_speed)
    screen.update()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.speed_up()
    # Detect collisions with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()
    # Detect when the ball missed the paddle
    if ball.xcor() > 390:
        # Right
        ball.ball_reset()
        scoreboard.increase_score_left()
    if ball.xcor() < -390:
        # Left
        ball.ball_reset()
        scoreboard.increase_score_right()

screen.exitonclick()
