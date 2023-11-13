from turtle import Turtle, Screen
from paddle import Paddle

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

paddle = Paddle()
screen.update()
screen.exitonclick()
