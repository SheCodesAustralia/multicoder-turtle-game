# superclass for world settings
#   set it up like a grid
# subclass has a different style

# could flash turtle red when tries to move into an obstacle
import turtle
from Turtle import CustomTurtle, UserTurtle
from worlds import WORLDS


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.screen = turtle.Screen()
        # self.myrtle = None

    def create_base_world(self):
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic('grid-white.gif')
        self.screen.bgcolor('pink')

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")

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

game.myrtle = UserTurtle(
    'red',
    2,
    game
)


turtle.mainloop()


# TODO
## lookup function for what is in the cell
