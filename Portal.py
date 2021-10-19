import turtle
from config import STEP_SIZE

STAMP_SIZE = 20


class Portal(turtle.Turtle):

    def __init__(self, colour, shape, position):
        super().__init__()
        self.color(colour)
        self.shape(shape)
        self.penup()
        self.goto(position)
        self.shapesize(STEP_SIZE/STAMP_SIZE)
