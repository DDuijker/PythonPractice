from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.create_paddle(x_position)

    def create_paddle(self, x_pos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, 0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



