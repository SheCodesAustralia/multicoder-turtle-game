import turtle
from MoveObject import MoveObject
import random


class CustomTurtle(turtle.Turtle, MoveObject):

    def __init__(self, colour, speed, game, start_position):
        super(CustomTurtle, self).__init__()
        MoveObject.__init__(self, game, start_position)
        self.color(colour)
        self.shape('turtle')
        self.speed(speed)
        self.game = game


class UserTurtle(CustomTurtle):

    def __init__(self, colour, speed, game):
        super().__init__(colour, speed, game, (0, 0))
        turtle.onkey(self.move_forward, 'Up')
        turtle.onkey(self.move_backward, 'Down')
        turtle.onkey(self.turn_left, 'Left')
        turtle.onkey(self.turn_right, 'Right')


class RobotTurtle(CustomTurtle):
    def __init__(self, colour, speed, game):
        super().__init__(colour, speed, game, (5, 5))

    def move(self):
        turning_angles = [0, 90, 270]
        for i in range(100):
            turning_angle = random.choice(turning_angles)
            current_direction = self.heading()
            self.setheading((current_direction + turning_angle))
            num_steps = random.randint(1, 5)
            for step in range(num_steps):
                self.move_forward()
                self.wait(5)
