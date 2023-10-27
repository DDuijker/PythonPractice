from turtle import Turtle
from random import random

tim = Turtle()

# Draw a triangle, square, pentagon, hexagon, heptagon, octa, nonagon and decagon, each a different colour
MAX_CORNERS = 10
amount_of_corners = 3

while amount_of_corners <= MAX_CORNERS:
    degrees = 360 / amount_of_corners
    tim.color(random(), random(), random())
    # Create the shape
    for _ in range(amount_of_corners):
        tim.forward(50)
        tim.right(degrees)
    amount_of_corners += 1
