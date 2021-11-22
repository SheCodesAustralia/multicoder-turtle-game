from config import CELL_WIDTH


def convert_coord_to_grid_pos(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    x = CELL_WIDTH * (0.5 + x)
    y = CELL_WIDTH * (0.5 + y)
    return (x, y)
