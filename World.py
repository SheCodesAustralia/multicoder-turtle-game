from utils import convert_coord_to_grid_pos
from Portal import Portal
from Obstacle import Obstacle


class World:

    def __init__(self, obstacle_positions=[], portal_position=(0, 0)):
        self.obstacle_positions = obstacle_positions
        self.portal_position = portal_position

    def draw_obstacles(self):
        for position in self.obstacle_positions:
            position = convert_coord_to_grid_pos(position)
            Obstacle('#136b0a', 'square', position)
    
    def draw_portal(self):
        portal_grid_position = convert_coord_to_grid_pos(self.portal_position)
        self.portal = Portal('blue', 'circle', portal_grid_position)


WORLDS = [
    World(
        obstacle_positions = [
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)
        ],
        portal_position=(10, 5)
    ),
    World(
        obstacle_positions = [
            (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5)
        ],
        portal_position=(6, 10)
    ),
    World(
        obstacle_positions = [
            (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)
        ],
        portal_position=(4, 3)
    )
]
