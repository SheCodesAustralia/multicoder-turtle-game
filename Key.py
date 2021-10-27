import turtle
from config import STEP_SIZE, STAMP_SIZE, FOOD


class Key(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(FOOD)
        self.speed(10)
        self.penup()
        self.goto(position)
        self.shapesize(STEP_SIZE/STAMP_SIZE)
