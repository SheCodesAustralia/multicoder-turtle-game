from utils import convert_coord_to_grid_pos
from Portal import Portal
from Obstacle import Obstacle


class World:

    def __init__(self, obstacle_positions=None, portal_position=None):
        self.obstacle_positions = obstacle_positions if obstacle_positions else []
        self.portal_position = portal_position if portal_position else (0, 0)

    def draw_obstacles(self):
        for position in self.obstacle_positions:
            position = convert_coord_to_grid_pos(position)
            Obstacle('#136b0a', 'square', position)

    def draw_portal(self):
        portal_grid_position = convert_coord_to_grid_pos(self.portal_position)
        self.portal = Portal('blue', 'circle', portal_grid_position)


# TODO lookup
