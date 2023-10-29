from turtle import Turtle

tim = Turtle()

# Make a dashed line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()