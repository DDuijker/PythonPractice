from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.start_x_pos = 0
        self.start_y_pos = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create 3 snake starting segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.segments.append(block)

    def elongate(self):
        """ Adds a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Loop through numbers in segments, start at 3, end at 0 and with a step of -1 (2,1,0)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Second to last segment position
            position = self.segments[seg_num - 1].pos()
            # Tell the segment to go to the second to last position
            self.segments[seg_num].goto(x=position[0], y=position[1])
        # Make the first segment move, causing the whole 'snake' to move forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
