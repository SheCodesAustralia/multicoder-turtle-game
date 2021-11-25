from utils import convert_coord_to_grid_pos
from Obstacle import Obstacle
from config import NUM_GRID_ROWS, FOOD, ROCK, PORTAL


class World:

    def __init__(self, obstacle_positions, portal_position, bird_start_position, food_position):
        self.obstacle_positions = obstacle_positions
        self.portal_position = portal_position
        self.bird_start_position = bird_start_position
        self.food_position = food_position
        self.food = None

    def draw_obstacles(self):
        ##
        position = convert_coord_to_grid_pos((0, 7))
        Obstacle(ROCK, position)
        position = convert_coord_to_grid_pos((1, 7))
        Obstacle(ROCK, position)
        position = convert_coord_to_grid_pos((2, 1))
        Obstacle(ROCK, position)
        position = convert_coord_to_grid_pos((2, 2))
        Obstacle(ROCK, position)
        position = convert_coord_to_grid_pos((3, 2))
        Obstacle(ROCK, position)
        position = convert_coord_to_grid_pos((3, 6))
        Obstacle(ROCK, position)
        ##
        pass

    def draw_portal(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def draw_food(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def cell_contains_portal(self, cell):
        ##
        # YOUR CODE HERE
        ##
        return False

    def cell_contains_obstacle(self, cell):
        ##
        if cell in self.obstacle_positions:
            return True
        if cell[0] < 0 or cell[0] >= NUM_GRID_ROWS:
            return True
        if cell[1] < 0 or cell[1] >= NUM_GRID_ROWS:
            return True
        ##
        return False

    def cell_contains_food(self, cell):
        ##
        # YOUR CODE HERE
        ##
        return False

    def cell_is_empty(self, cell):
        ##
        if self.cell_contains_obstacle(cell):
            return False
        ##
        return True
