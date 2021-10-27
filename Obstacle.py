import turtle
from config import STEP_SIZE, STAMP_SIZE, ROCK


class Obstacle(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(ROCK)
        self.speed(10)
        self.penup()
        self.shapesize(STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE)
        self.goto(position)
