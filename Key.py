import turtle
from config import STEP_SIZE

STAMP_SIZE = 20


class Key(turtle.Turtle):

    def __init__(self, colour, shape, position):
        super().__init__()
        self.color(colour)
        self.shape(shape)
        self.speed(10)
        self.penup()
        self.goto(position)
        self.shapesize(STEP_SIZE/STAMP_SIZE)
