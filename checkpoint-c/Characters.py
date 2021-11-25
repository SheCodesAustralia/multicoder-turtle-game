import turtle
from MoveObject import MoveObject
import random


class CustomTurtle(turtle.Turtle, MoveObject):

    def __init__(self, colour, shape, speed, game, allowed_through_portal, start_position):
        super(CustomTurtle, self).__init__()
        MoveObject.__init__(self, game, allowed_through_portal, start_position)
        self.game = game
        self.color(colour)
        self.shape(shape)
        self.speed(speed)


class UserTurtle(CustomTurtle):

    def __init__(self, colour, shape, speed, game, start_position):
        super().__init__(colour, shape, speed, game, True, start_position)
        ##
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.move_forward, 'Up')
        ##


class RobotBird(CustomTurtle):
    def __init__(self, colour, shape, speed, game, start_position):
        super().__init__(colour, shape, speed, game, False, start_position)
        ##
        # YOUR CODE HERE
        ##

    def move(self):
        ##
        # YOUR CODE HERE
        ##
        pass
