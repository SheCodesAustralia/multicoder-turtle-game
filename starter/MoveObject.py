from config import STEP_SIZE
from utils import convert_coord_to_grid_pos


class MoveObject:

    def __init__(self, game, allowed_through_portal, start_position):
        self.game = game
        self.start_position = start_position
        self.current_position = start_position
        self.allowed_through_portal = allowed_through_portal
        ##
        # YOUR CODE HERE
        ##
    
    def get_up_position(self):
        pass

    def get_right_position(self):
        pass

    def get_down_position(self):
        pass

    def get_left_position(self):
        pass

    def get_possible_positions(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def move_forward(self):
        ##
        # YOUR CODE HERE
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
        # YOUR CODE HERE
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
        # YOUR CODE HERE
        ##
        pass

    def eat_food(self):
        ##
        # YOUR CODE HERE
        ##
        pass
