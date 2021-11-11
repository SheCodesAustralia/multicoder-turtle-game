import turtle
from config import STEP_SIZE, STAMP_SIZE


class Obstacle(turtle.Turtle):

    def __init__(self, shape, position):
        super().__init__()
        self.hideturtle()
        self.speed(10)
        self.shape(shape)
        self.penup()
        self.shapesize(STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE, STEP_SIZE/STAMP_SIZE)
        self.goto(position)
        self.showturtle()
