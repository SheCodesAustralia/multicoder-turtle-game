import turtle
from config import STEP_SIZE, STAMP_SIZE, TREE


class Obstacle(turtle.Turtle):

    def __init__(self, colour, shape, position):
        super().__init__()
        self.color(colour)
        self.shape(TREE)
        self.speed(10)
        self.penup()
        self.shapesize(STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE)
        self.goto(position)
