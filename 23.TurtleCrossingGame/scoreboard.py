from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.penup()
        self.goto(x=-280, y=250)
        self.hideturtle()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)
