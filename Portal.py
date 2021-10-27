import turtle
from config import STEP_SIZE, STAMP_SIZE, UMBRELLA


class Portal(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(UMBRELLA)
        self.penup()
        self.goto(position)
        self.shapesize(STEP_SIZE/STAMP_SIZE)
