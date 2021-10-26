import turtle
from MoveObject import MoveObject
import random


class CustomTurtle(turtle.Turtle, MoveObject):

    def __init__(self, colour, speed, game, allowed_through_portal, start_position):
        super(CustomTurtle, self).__init__()
        MoveObject.__init__(self, game, allowed_through_portal, start_position)
        self.color(colour)
        self.speed(speed)
        self.game = game
        self.has_key = False


class UserTurtle(CustomTurtle):

    def __init__(self, colour, speed, game, start_position):
        super().__init__(colour, speed, game, True, start_position)
        self.shape('turtle')
        turtle.onkey(self.move_forward, 'Up')
        turtle.onkey(self.move_backward, 'Down')
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.turn_right, 'Right')


class RobotTurtle(CustomTurtle):
    def __init__(self, colour, speed, game, start_position):
        super().__init__(colour, speed, game, False, start_position)
        self.game = game

    def move(self):
        turning_angles = self.get_possible_positions()
        turning_angle = random.choice(turning_angles)
        current_direction = self.heading()
        self.setheading(current_direction + turning_angle)
        num_steps = random.randint(1, 5)
        for step in range(num_steps):
            self.move_forward()
