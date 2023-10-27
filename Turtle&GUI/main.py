import colorgram
import turtle as t
import random as r

# Extract 100 colours from the image
colors = colorgram.extract('spot_painting.jpg', 100)
rgb_values = []
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()

# Starting position
# Somewhere between 270 and 180
tim.setheading(225)
tim.forward(300)
# Get it to face right again
tim.setheading(0)

# Return a list with each colour being a rgb colour tuple from the image
for color in colors:
    # If the colour is too close to being completely white, skip it
    if color.rgb.r > 240 and color.rgb.g > 240 and color.rgb.b > 240:
        pass
    else:
        rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_values.append(rgb_color)

t.colormode(255)

# 100 dots
for dot_count in range(1, 101):
    tim.dot(20, r.choice(rgb_values))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
