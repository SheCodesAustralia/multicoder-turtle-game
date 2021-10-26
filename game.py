import turtle
from Turtle import UserTurtle, RobotTurtle
from worlds import WORLDS
from config import TREE, KEY, PORTAL, BIRD, OCEAN


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.screen = turtle.Screen()

    def create_base_world(self):
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic('assets/grid-white.gif')
        self.screen.bgcolor('black')
        self.screen.addshape(TREE)
        self.screen.addshape(KEY)
        self.screen.addshape(PORTAL)
        self.screen.addshape(BIRD)

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
    
    def create_user_turtle(self):
        self.myrtle = UserTurtle(
            1,
            'red',
            self,
            self.current_world.portal_position
        )
        self.myrtle.x_pos = self.current_world.portal_position[0]
        self.myrtle.y_pos = self.current_world.portal_position[1]
    
    def create_robot_turlte(self):
        self.flippy = RobotTurtle(
            10,
            'grey',
            self,
            self.current_world.robot_start_position
        )
        self.flippy.x_pos = self.current_world.robot_start_position[0]
        self.flippy.y_pos = self.current_world.robot_start_position[1]

    def find_next_world(self):
        self.clear_world()
        self.create_user_turtle()
        self.world += 1
        # if (self.world == 1):
        #     self.game_end()
        # else:
        self.current_world = WORLDS[self.world]
        self.create_robot_turlte()
        self.draw_world()
        self.flippy.move()

    # TODO
    def game_end(self):
        turtle.clearscreen()
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(OCEAN)



turtle.listen()

game = Game()
game.create_base_world()
# game.game_end()
game.draw_world()

game.myrtle = UserTurtle(
    'red',
    1,
    game,
    (0, 0)
)

game.flippy = RobotTurtle(
    'grey',
    1,
    game,
    game.current_world.robot_start_position
)
# game.flippy.move()

game.pecky = RobotTurtle(
    'red',
    3,
    game,
    (5, 5)
)

while True:
    game.pecky.move()
    game.flippy.move()
# game.screen.ontimer(game.pecky.move(), 10)
# game.screen.ontimer(game.flippy.move(), 10)
# turtle.ontimer(game.flippy.move(), 10)
# turtle.ontimer(game.pecky.move(), 10)
# game.pecky.move()

# turtle.mainloop()
