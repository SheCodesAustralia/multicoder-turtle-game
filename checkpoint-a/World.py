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
        # YOUR CODE HERE
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
        # YOUR CODE HERE
        ##
        return False

    def cell_contains_food(self, cell):
        ##
        # YOUR CODE HERE
        ##
        return False

    def cell_is_empty(self, cell):
        ##
        # YOUR CODE HERE
        ##
        return True
