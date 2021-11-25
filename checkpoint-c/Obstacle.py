import turtle
from config import CELL_WIDTH, STAMP_SIZE


class Obstacle(turtle.Turtle):

    def __init__(self, shape, position):
        super().__init__()
        ##
        self.hideturtle()
        self.speed(10)
        self.shape(shape)
        self.penup()
        self.shapesize(CELL_WIDTH/STAMP_SIZE, CELL_WIDTH/STAMP_SIZE, CELL_WIDTH/STAMP_SIZE)
        self.goto(position)
        self.showturtle()
        ##
