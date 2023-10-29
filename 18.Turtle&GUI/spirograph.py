# from turtle import Turtle, Screen
import turtle as t
from random import *

tim = t.Turtle()
t.colormode(255)
tim.shape("circle")


def random_color():
    """Returns a random rgb value between 1 and 255 as a tuple"""
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return r, g, b


# Make a spirograph
tim.speed("fastest")
tim.hideturtle()


def draw_spirograph(size_of_gap):
    """Draws a spirograph using a gap_size to determine the tilt"""
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5.0)

screen = t.Screen()
screen.exitonclick()
