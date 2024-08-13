from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 80, 'normal')
LEFT_POSITION = (-100, 200)
RIGHT_POSITION = (100, 200)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def increase_score_right(self):
        self.clear()
        self.right_score += 1
        self.update_scoreboard()

    def increase_score_left(self):
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def write_score(self, score, position):
        self.goto(position)
        self.write(score, align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.write_score(self.left_score, LEFT_POSITION)
        self.write_score(self.right_score, RIGHT_POSITION)

