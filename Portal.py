import turtle
from config import STEP_SIZE, STAMP_SIZE, PORTAL


class Portal(turtle.Turtle):

    def __init__(self, colour, shape, position):
        super().__init__()
        self.color(colour)
        self.shape(PORTAL)
        self.penup()
        self.goto(position)
        self.shapesize(STEP_SIZE/STAMP_SIZE)
