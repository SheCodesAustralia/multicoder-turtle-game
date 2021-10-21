# superclass for world settings
#   set it up like a grid
# subclass has a different style

# could flash turtle red when tries to move into an obstacle
import turtle
from Turtle import CustomTurtle
from worlds import WORLDS


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        # self.myrtle = None

    def create_base_world(self):
        screen = turtle.Screen()
        screen.setup(520, 520)
        screen.setworldcoordinates(0, 0, 500, 500)
        screen.bgpic('grid-white.gif')
        screen.bgcolor('pink')

        canvas = screen.getcanvas()
        canvas.itemconfig(screen._bgpic, anchor="sw")

        self.draw_world()

    def draw_world(self):
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()

    # TODO
    def clear_world(self):
        pass

    def find_next_world(self):
        print('cats')
        self.world += 1
        self.current_world = WORLDS[self.world]

        self.draw_world()


turtle.listen()

game = Game()
game.create_base_world()


# game.myrtle.color('red')

game.myrtle = CustomTurtle(
    'red',
    2,
    game
)
game.myrtle.goto_start_position()


turtle.mainloop()


# TODO
## lookup function for what is in the cell
