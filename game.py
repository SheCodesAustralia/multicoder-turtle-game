import turtle
from Turtle import UserTurtle, RobotTurtle
from worlds import WORLDS


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
        self.current_world.draw_key()

    def clear_world(self):
        # clear the screen and redraw the turtle
        turtle.clearscreen()
        self.create_base_world()
        self.myrtle = UserTurtle(
            'red',
            2,
            self,
            self.current_world.portal_position
        )
        self.myrtle.x_pos = self.current_world.portal_position[0]
        self.myrtle.y_pos = self.current_world.portal_position[1]
        self.flippy = RobotTurtle(
            'purple',
            self,
            self.current_world.robot_start_position
        )
        self.flippy.x_pos = self.current_world.robot_start_position[0]
        self.flippy.y_pos = self.current_world.robot_start_position[1]

    def find_next_world(self):
        self.clear_world()
        self.world += 1
        self.current_world = WORLDS[self.world]
        self.draw_world()
        self.flippy.move()


turtle.listen()

game = Game()
game.create_base_world()
game.draw_world()

game.myrtle = UserTurtle(
    'red',
    2,
    game
)

game.flippy = RobotTurtle(
    'purple',
    game
)
# game.flippy.move()

turtle.mainloop()
