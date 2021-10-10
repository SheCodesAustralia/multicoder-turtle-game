# superclass for world settings
#   set it up like a grid
# subclass has a different style

# could flash turtle red when tries to move into an obstacle


import turtle
from BaseWorld import create_base_world
from Turtle import CustomTurtle
from Obstacle import Obstacle
from config import STEP_SIZE, OBSTACLE_POSITIONS


def convert_coord_to_grid_pos(coordinates):
    x, y = coordinates
    if x == 0:
        x = STEP_SIZE * 0.5
    else:
        x = STEP_SIZE * (0.5 + x)
    if y == 0:
        y = STEP_SIZE * 0.5
    else:
        y = STEP_SIZE * (0.5 + y)
    return (x, y)


create_base_world()

myrtle = CustomTurtle('blue', 2)

myrtle.goto(STEP_SIZE/2, STEP_SIZE/2)

turtle.listen()

turtle.onkey(myrtle.move_forward, 'Up')
turtle.onkey(myrtle.move_backward, 'Down')
turtle.onkey(myrtle.turn_left, 'Left')
turtle.onkey(myrtle.turn_right, 'Right')


for position in OBSTACLE_POSITIONS:
    position = convert_coord_to_grid_pos(position)
    Obstacle('#136b0a', 'square', position)


turtle.mainloop()
