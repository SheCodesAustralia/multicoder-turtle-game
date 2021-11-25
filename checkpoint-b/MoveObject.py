from config import CELL_WIDTH
from utils import convert_coord_to_grid_pos


class MoveObject:

    def __init__(self, game, allowed_through_portal, start_position):
        self.game = game
        self.start_position = start_position
        self.current_position = start_position
        self.allowed_through_portal = allowed_through_portal
        ##
        self.goto_start_position()
        ##

    def get_up_position(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def get_right_position(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def get_down_position(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def get_left_position(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def get_possible_positions(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def move_forward(self):
        ##
        self.forward(CELL_WIDTH)
        ##
        pass

    def is_collision(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def move_backward(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def turn_right(self):
        ##
        self.left(90)
        ##
        pass

    def turn_left(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def enter_portal(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def goto_start_position(self):
        ##
        self.penup()
        self.hideturtle()
        self.current_position = self.start_position
        start_position = convert_coord_to_grid_pos(self.start_position)
        self.goto(start_position)
        self.showturtle()
        ##
        pass

    def eat_food(self):
        ##
        # YOUR CODE HERE
        ##
        pass
