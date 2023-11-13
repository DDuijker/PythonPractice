from turtle import Turtle

LEFT_POSITIONS = [(-350, 40), (-350, 20), (-350, 0), (-350, -20), (-350, -40)]
RIGHT_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.left_segments = []
        self.right_segments = []
        self.create_paddles()

    def create_paddles(self):
        # Create the left paddle
        for position in LEFT_POSITIONS:
            self.add_segment(position, self.left_segments)
        # Create the right paddle
        for position in RIGHT_POSITIONS:
            self.add_segment(position, self.right_segments)

    def add_segment(self, position, segment_list):
        p_piece = Turtle("square")
        p_piece.color("white")
        p_piece.penup()
        p_piece.goto(position)
        segment_list.append(p_piece)



