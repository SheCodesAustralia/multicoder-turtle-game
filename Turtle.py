import turtle
from config import STEP_SIZE
from MoveObject import MoveObject


class CustomTurtle(turtle.Turtle, MoveObject):

    def __init__(self, colour, speed, game):
        super(CustomTurtle, self).__init__()
        # MoveObject.__init__(self)
        self.set_start_position()
        self.color(colour)
        self.shape('turtle')
        self.speed(speed)
        self.game = game


class UserTurtle(CustomTurtle):

    def __init__(self, *args, **kwargs): # color/speed/etc
        super().__init__(*args, **kwargs)
        turtle.onkey(self.move_forward, 'Up')
        turtle.onkey(self.move_backward, 'Down')
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.turn_right, 'Right')
        self.goto_start_position(STEP_SIZE/2, STEP_SIZE/2)
