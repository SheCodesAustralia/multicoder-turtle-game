# superclass for world settings
#   set it up like a grid
# subclass has a different style

# could flash turtle red when tries to move into an obstacle
import turtle
from Turtle import UserTurtle
from worlds import WORLDS
from config import STEP_SIZE


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.screen = turtle.Screen()

    def create_base_world(self):
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic('grid-white.gif')
        self.screen.bgcolor('pink')

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")

    def draw_world(self):
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()

    def clear_world(self):
        turtle.clearscreen()
        game.myrtle = UserTurtle(
            'red',
            2,
            game
        )
        self.myrtle.goto(STEP_SIZE/1, STEP_SIZE/2)
        self.create_base_world()

    def find_next_world(self):
        self.world += 1
        self.current_world = WORLDS[self.world]
        self.clear_world()
        self.draw_world()


turtle.listen()

game = Game()
game.create_base_world()
game.draw_world()

game.myrtle = UserTurtle(
    'red',
    2,
    game
)

turtle.mainloop()
