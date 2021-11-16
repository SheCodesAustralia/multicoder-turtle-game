from config import STEP_SIZE
from utils import convert_coord_to_grid_pos


class MoveObject:

    def __init__(self, game, allowed_through_portal, start_position):
        self.game = game
        self.start_position = start_position
        self.current_position = start_position
        self.allowed_through_portal = allowed_through_portal
        self.goto_start_position()

    def get_possible_positions(self):
        up_position = self.get_up_position()
        right_position = self.get_right_position()
        left_position = self.get_left_position()
        down_position = self.get_down_position()
        valid_directions = []
        if self.game.current_world.cell_is_empty(up_position):
            valid_directions.append(90)
        if self.game.current_world.cell_is_empty(right_position):
            valid_directions.append(0)
        if self.game.current_world.cell_is_empty(down_position):
            valid_directions.append(270)
        if self.game.current_world.cell_is_empty(left_position):
            valid_directions.append(180)
        return valid_directions

    def get_up_position(self):
        return (self.current_position[0], self.current_position[1] + 1)

    def get_right_position(self):
        return (self.current_position[0] + 1, self.current_position[1])

    def get_down_position(self):
        return (self.current_position[0], self.current_position[1] - 1)

    def get_left_position(self):
        return (self.current_position[0] - 1, self.current_position[1])

    def move_forward(self):
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = self.get_up_position()
        if direction == 0.0:  # facing right
            new_pos = self.get_right_position()
        if direction == 270.0:  # facing down
            new_pos = self.get_down_position()
        if direction == 180.0:  # facing left
            new_pos = self.get_left_position()

        # check there is no obstacle there
        if self.game.current_world.cell_is_empty(new_pos):
            self.current_position = new_pos
            self.forward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos):
                self.current_position = new_pos
                self.forward(STEP_SIZE)
                self.enter_portal()
            if self.game.current_world.cell_contains_food(new_pos):
                self.current_position = new_pos
                self.forward(STEP_SIZE)
                self.eat_food()

        if self.is_collision():
            self.game.score = self.game.score - 5
            self.game.update_score()
            self.game.myrtle.goto_start_position()

    def is_collision(self):
        for bird in self.game.birds:
            if self.game.myrtle.current_position == bird.current_position:
                return True
        return False

    def move_backward(self):  # challenge for them to add themselves?
        # figure out new position
        direction = self.heading()
        if direction == 90.0:  # facing up
            new_pos = self.get_down_position()
        if direction == 0.0:  # facing right
            new_pos = self.get_left_position()
        if direction == 270.0:  # facing down
            new_pos = self.get_up_position()
        if direction == 180.0:  # facing left
            new_pos = self.get_right_position()

        # check there is no obstacle there
        if not self.game.current_world.cell_is_empty(new_pos):
            self.current_position = new_pos
            self.backward(STEP_SIZE)

        if self.allowed_through_portal:
            if self.game.current_world.cell_contains_portal(new_pos):
                self.current_position = new_pos
                self.backward(STEP_SIZE)
                self.enter_portal()
            if self.game.current_world.cell_contains_food(new_pos):
                self.current_position = new_pos
                self.backward(STEP_SIZE)
                self.eat_food()

        if self.is_collision():
            self.game.score = self.game.score - 5
            self.game.update_score()
            self.game.myrtle.goto_start_position()

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def enter_portal(self):
        self.game.find_next_world()

    def goto_start_position(self):
        self.penup()
        self.hideturtle()
        self.current_position = self.start_position
        start_position = convert_coord_to_grid_pos(self.start_position)
        self.goto(start_position)
        self.showturtle()

    def eat_food(self):
        self.game.score = self.game.score + 5
        self.game.update_score()
        self.game.current_world.food.hideturtle()
