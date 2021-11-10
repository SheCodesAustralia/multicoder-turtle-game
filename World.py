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
        for position in self.obstacle_positions:
            position = convert_coord_to_grid_pos(position)
            Obstacle(ROCK, position)

    def draw_portal(self):
        portal_grid_position = convert_coord_to_grid_pos(self.portal_position)
        Obstacle(PORTAL, portal_grid_position)

    def draw_food(self):
        food_grid_position = convert_coord_to_grid_pos(self.food_position)
        self.food = Obstacle(FOOD, food_grid_position)

    def cell_contains_portal(self, cell):
        if cell == self.portal_position:
            return True
        return False

    def cell_contains_obstacle(self, cell):
        if cell in self.obstacle_positions:
            return True
        if cell[0] < 0 or cell[0] >= NUM_GRID_ROWS:
            return True
        if cell[1] < 0 or cell[1] >= NUM_GRID_ROWS:
            return True
        return False

    def cell_contains_food(self, cell):
        if cell == self.food_position:
            return True
        return False

    def cell_is_empty(self, cell):
        return not self.cell_contains_portal(cell) and \
            not self.cell_contains_food(cell) and \
                not self.cell_contains_obstacle(cell)
