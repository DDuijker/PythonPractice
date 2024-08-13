from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """ Creates a car as a turtle, Has a one in 6 chance of creation, to reduce the amount made in the game."""
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            # Give a car a random color
            new_car.color(random.choice(COLORS))
            # Let the car go to a random spot on the y-axis between -280 and +280.
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            # Let the car move from right to left
            car.forward(self.car_speed)

    def go_faster(self):
        self.car_speed += MOVE_INCREMENT
