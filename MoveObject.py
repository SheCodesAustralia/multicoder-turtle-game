from config import STEP_SIZE
from utils import convert_coord_to_grid_pos


class MoveObject:

    def __init__(self, game, allowed_through_portal, start_position):
        self.game = game
        self.x_pos = start_position[0]
        self.y_pos = start_position[1]
        self.allowed_through_portal = allowed_through_portal
        self.goto_start_position(start_position)
    
    def get_possible_positions(self):
        # self.move_forward()
        # direction = self.heading()
        up_position = (self.x_pos, self.y_pos + 1)
        right_position = (self.x_pos + 1, self.y_pos)
        left_position = (self.x_pos - 1, self.y_pos)
        
        valid_directions = []
        if self.game.current_world.cell_is_empty(up_position):
            valid_directions.append(0)
        if self.game.current_world.cell_is_empty(right_position):
            valid_directions.append(90)
        if self.game.current_world.cell_is_empty(left_position):
            valid_directions.append(270)
        return valid_directions

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
        if not self.game.current_world.cell_contains_obstacle(new_pos):
            if not self.game.current_world.cell_contains_portal(new_pos) and \
                not self.game.current_world.cell_contains_key(new_pos):
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.forward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos) and \
                self.game.myrtle.has_key:
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.forward(STEP_SIZE)
                self.enter_portal()    
            if self.game.current_world.cell_contains_key(new_pos):
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.forward(STEP_SIZE)
                self.pickup_key()

    def move_backward(self):  # challenge for them to add themselves?
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
        if not self.game.current_world.cell_contains_obstacle(new_pos):
            if not self.game.current_world.cell_contains_portal(new_pos) and \
                not self.game.current_world.cell_contains_key(new_pos):
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.backward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos) and \
                self.game.myrtle.has_key:
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.backward(STEP_SIZE)
                self.enter_portal()    
            if self.game.current_world.cell_contains_key(new_pos):
                self.x_pos = new_pos[0]
                self.y_pos = new_pos[1]
                self.backward(STEP_SIZE)
                self.pickup_key()

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def enter_portal(self):
        self.game.find_next_world()

    def goto_start_position(self, coordinates):
        self.penup()
        start_position = convert_coord_to_grid_pos(coordinates)
        self.goto(start_position[0], start_position[1])

    def pickup_key(self):
        self.game.current_world.key.hideturtle()
        self.game.myrtle.color('orange')
        self.game.myrtle.has_key = True
