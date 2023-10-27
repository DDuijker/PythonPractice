import colorgram
import turtle as t
import random as r

# Extract 100 colours from the image
colors = colorgram.extract('spot_painting.jpg', 100)
rgb_values = []
tim = t.Turtle()

# Return a list with each colour being a rgb colour tuple from the image
for color in colors:
    # If the colour is too close to being completely white, skip it
    if color.rgb.r > 240 and color.rgb.g > 240 and color.rgb.b > 240:
        pass
    else:
        rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_values.append(rgb_color)

t.colormode(255)


def put_dot():
    """Function to put a dot the size of 20 with a random color"""
    tim.pendown()
    tim.pencolor(r.choice(rgb_values))
    tim.dot(20)
    tim.penup()


# 10 by 10 rows of spots
for row in range(10):
    for dot in range(10):
        # make a dot with a random color
        put_dot()
        # And 50 spaces apart
        tim.fd(50)
    # Alternate between left and right when going up
    if row % 2 == 0:
        put_dot()
        tim.left(90)
        tim.fd(50)
        tim.left(90)
    else:
        put_dot()
        tim.right(90)
        tim.fd(50)
        tim.right(90)


screen = t.Screen()
screen.exitonclick()
