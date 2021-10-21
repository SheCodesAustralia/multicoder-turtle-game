from utils import convert_coord_to_grid_pos
from Portal import Portal
from Obstacle import Obstacle
from config import NUM_GRID_ROWS


class World:

    def __init__(self, obstacle_positions=None, portal_position=None):
        if obstacle_positions:
            self.obstacle_positions = obstacle_positions
        else:
            self.obstacle_positions = []
        if portal_position:
            self.portal_position = portal_position
        else:
            self.portal_positions = (0, 0)
        self.portal = None

    def draw_obstacles(self):
        for position in self.obstacle_positions:
            position = convert_coord_to_grid_pos(position)
            Obstacle('#136b0a', 'square', position)

    def draw_portal(self):
        portal_grid_position = convert_coord_to_grid_pos(self.portal_position)
        self.portal = Portal('blue', 'circle', portal_grid_position)

    def cell_has_portal(self, cell):
        if cell == self.portal_position:
            return True
        return False

    def cell_has_obstacle(self, cell):
        if cell in self.obstacle_positions:
            return True
        if cell[0] < 0 or cell[0] >= NUM_GRID_ROWS:
            return True
        if cell[1] < 0 or cell[1] >= NUM_GRID_ROWS:
            return True
        return False
