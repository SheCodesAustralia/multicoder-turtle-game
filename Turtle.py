import turtle
from config import STEP_SIZE, OBSTACLE_POSITIONS, NUM_GRID_ROWS


class CustomTurtle(turtle.Turtle):

    def __init__(self, colour, speed):
        super().__init__()
        self.color(colour)
        self.speed(speed)
        self.shape('turtle')
        self.penup()
        self.x_pos = 0
        self.y_pos = 0

    def move_forward(self):
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = (self.x_pos, self.y_pos + 1)
        if direction == 0.0:  # facing right
            new_pos = (self.x_pos + 1, self.y_pos)
        if direction == 270.0:  # facing down
            new_pos = (self.x_pos, self.y_pos - 1)
        if direction == 180.0:  # facing left
            new_pos = (self.x_pos - 1, self.y_pos)

        # check there is no obstacle there
        if self.is_clear(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.forward(STEP_SIZE)

    def move_backward(self):
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = (self.x_pos, self.y_pos - 1)
        if direction == 0.0:  # facing right
            new_pos = (self.x_pos - 1, self.y_pos)
        if direction == 270.0:  # facing down
            new_pos = (self.x_pos, self.y_pos + 1)
        if direction == 180.0:  # facing left
            new_pos = (self.x_pos + 1, self.y_pos)

        # check there is no obstacle there
        if self.is_clear(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.backward(STEP_SIZE)

    def turn_right(self):
        self.right(90)
        print(self.heading())

    def turn_left(self):
        self.left(90)
        print(self.heading())

    def is_clear(self, new_pos):
        print(new_pos)
        print(new_pos not in OBSTACLE_POSITIONS)
        if new_pos in OBSTACLE_POSITIONS:
            return False
        if new_pos[0] < 0 or new_pos[0] > 10:
            return False
        if new_pos[1] < 0 or new_pos[1] > 10:
            return False
        return True
