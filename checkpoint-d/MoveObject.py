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
        return (self.current_position[0], self.current_position[1] + 1)
        ##
        pass

    def get_right_position(self):
        ##
        return (self.current_position[0] + 1, self.current_position[1])
        ##
        pass

    def get_down_position(self):
        ##
        return (self.current_position[0], self.current_position[1] - 1)
        ##
        pass

    def get_left_position(self):
        ##
        return (self.current_position[0] -1, self.current_position[1])
        ##
        pass

    def get_possible_positions(self):
        ##
        up_position = self.get_up_position()
        right_position = self.get_right_position()
        left_position = self.get_left_position()
        down_position = self.get_down_position()

        valid_directions = []
        if self.game.current_world.cell_is_empty(up_position):
            valid_directions.append(90)
            if self.game.current_world.cell_is_empty(some_position):
            valid_directions.append(x)
        if self.game.current_world.cell_is_empty(some_position):
            valid_directions.append(x)
        if self.game.current_world.cell_is_empty(some_position):
            valid_directions.append(x)
        return valid_directions
        ##
        pass

    def move_forward(self):
        ##
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = self.get_up_position()
        if direction == 0.0:  # facing right
            new_pos = self.get_right_position()
        if direction == 270.0:  # facing down
            new_pos = self.get_down_position()
        if direction == 180.0:  # facing left
            new_pos = self.get_left_position()
        if self.game.current_world.cell_is_empty(new_pos):
            self.current_position = new_pos
            self.forward(CELL_WIDTH)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos):
                self.current_position = new_pos
                self.forward(CELL_WIDTH)
                self.enter_portal()

        if self.is_collision():
            self.game.myrtle.goto_start_position()
        ##
        pass

    def is_collision(self):
        ##
        if self.game.myrtle.current_position == self.game.bird.current_position:
            return True
        return False
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
        self.game.find_next_world()
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
