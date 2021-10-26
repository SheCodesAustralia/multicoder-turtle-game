from utils import convert_coord_to_grid_pos
from Portal import Portal
from Obstacle import Obstacle
from Key import Key
from config import NUM_GRID_ROWS


class World:

    def __init__(self, obstacle_positions, portal_position, robot_start_position, key_position):
        self.obstacle_positions = obstacle_positions
        self.portal_position = portal_position
        self.robot_start_position = robot_start_position
        self.key_position = key_position
        self.key = None

    def draw_obstacles(self):
        for position in self.obstacle_positions:
            position = convert_coord_to_grid_pos(position)
            Obstacle('#136b0a', 'square', position)

    def draw_portal(self):
        portal_grid_position = convert_coord_to_grid_pos(self.portal_position)
        Portal('blue', 'circle', portal_grid_position)

    def draw_key(self):
        key_grid_position = convert_coord_to_grid_pos(self.key_position)
        self.key = Key('orange', 'circle', key_grid_position)

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

    def cell_contains_key(self, cell):
        if cell == self.key_position:
            return True
        return False

    def cell_is_empty(self, cell):
        return not self.cell_contains_portal(cell) and \
            not self.cell_contains_key(cell) and \
                not self.cell_contains_obstacle(cell)
