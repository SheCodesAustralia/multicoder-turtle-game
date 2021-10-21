from config import STEP_SIZE, NUM_GRID_ROWS

class MoveObject:

    def __init__(self, game):
        self.game = game
        self.x_pos = 0
        self.y_pos = 0
    
    def set_start_position(self):
        pass

    def move_forward(self):
        # figure out new position
        direction = self.heading()
        print(self.x_pos, self.y_pos)
        if direction == 90.0:  # facing up
            new_pos = (self.x_pos, self.y_pos + 1)
        if direction == 0.0:  # facing right
            new_pos = (self.x_pos + 1, self.y_pos)
        if direction == 270.0:  # facing down
            new_pos = (self.x_pos, self.y_pos - 1)
        if direction == 180.0:  # facing left
            new_pos = (self.x_pos - 1, self.y_pos)

        # check there is no obstacle there
        if not self.game.current_world.cell_has_obstacle(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.forward(STEP_SIZE)
            if self.game.current_world.cell_has_portal(new_pos):
                self.enter_portal()

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
        if not self.game.current_world.cell_has_obstacle(new_pos):
            self.x_pos = new_pos[0]
            self.y_pos = new_pos[1]
            self.backward(STEP_SIZE)
            if self.game.current_world.cell_has_portal(new_pos):
                self.enter_portal()

    def turn_right(self):
        self.right(90)

    def turn_left(self):
        self.left(90)

    def enter_portal(self):
        self.game.find_next_world()

    def goto_start_position(self, x_pos, y_pos):
        self.penup()
        self.goto(x_pos, y_pos)
