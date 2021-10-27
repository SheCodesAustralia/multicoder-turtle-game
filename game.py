import turtle
from Turtle import UserTurtle, RobotTurtle
from worlds import WORLDS
from config import ROCK, BIRD, OCEAN, GRID, UMBRELLA, FOOD


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.screen = turtle.Screen()
        self.birds = []

    def create_base_world(self):
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(GRID)
        self.screen.bgcolor('black')
        self.screen.addshape(ROCK)
        self.screen.addshape(BIRD)
        self.screen.addshape(UMBRELLA)
        self.screen.addshape(FOOD)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")

    def draw_world(self):
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()
        self.current_world.draw_key()

    def clear_world(self):
        turtle.clearscreen()
        self.birds = []
        self.create_base_world()

    def create_user_turtle(self):
        self.myrtle = UserTurtle(
            'red',
            1,
            self,
            self.current_world.portal_position
        )
        self.myrtle.position = self.current_world.portal_position

    def create_robot_turtle(self):
        flippy = RobotTurtle(
            'grey',
            'classic',
            3,
            self,
            self.current_world.robot_start_position
        )
        flippy.position = self.current_world.robot_start_position
        self.birds.append(flippy)

    def find_next_world(self):
        self.clear_world()
        if (self.world == 1):
            self.game_end()
        else:
            self.create_user_turtle()
            self.world += 1
            self.current_world = WORLDS[self.world]
            self.create_robot_turtle()
            self.draw_world()
            for bird in self.birds:
                bird.move()

    def game_end(self):
        turtle.clearscreen()
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(OCEAN)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")

        self.myrtle = RobotTurtle(
            '#402e08',
            'turtle',
            1,
            self,
            self.current_world.portal_position
        )
        while True:
            self.myrtle.move()


turtle.listen()

game = Game()
game.create_base_world()
game.draw_world()

game.myrtle = UserTurtle(
    '#402e08',
    3,
    game,
    (0, 0)
)

for i in range(2):
    bird = RobotTurtle(
        '#595957',
        'classic',
        3,
        game,
        (5, 5)
    )
    game.birds.append(bird)

while True:
    for bird in game.birds:
        bird.move()


# turtle.mainloop()
