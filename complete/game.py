import turtle
from Characters import UserTurtle, RobotBird
from worlds import WORLDS
from config import ROCK, BIRD, OCEAN, GRID, PORTAL, FOOD


class Game:

    def __init__(self):
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.screen = turtle.Screen()
        self.birds = []
        self.score = 0
        self.score_display = turtle.Turtle()

    def create_base_world(self):
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(GRID)
        self.screen.bgcolor('black')
        self.screen.addshape(ROCK)
        self.screen.addshape(BIRD)
        self.screen.addshape(PORTAL)
        self.screen.addshape(FOOD)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor='sw')
        self.update_score()

    def draw_world(self):
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()
        self.current_world.draw_food()
    
    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f'Score: {self.score}', font=('Arial', 16, 'normal'))

    def clear_world(self):
        turtle.clearscreen()
        self.birds = []
        self.create_base_world()

    def create_user_turtle(self, start_position):
        self.myrtle = UserTurtle(
            colour='#402e08',
            shape='turtle',
            speed=2,
            game=self,
            start_position=start_position
        )

    def create_robot_bird(self):
        bird = RobotBird(
            colour='#000000',
            shape='classic',
            speed=3,
            game=self,
            start_position=self.current_world.bird_start_position
        )
        self.birds.append(bird)

    def find_next_world(self):
        if (self.world == len(WORLDS) - 1):
            self.game_end()
        else:
            self.clear_world()
            user_turtle_start_position = self.current_world.portal_position
            self.score = self.score + 10
            self.update_score()
            self.world = self.world + 1
            self.current_world = WORLDS[self.world]
            self.draw_world()
            num_birds = self.world + 1
            for count in range(num_birds):
                self.create_robot_bird()
            for bird in self.birds:
                bird.move()
            self.create_user_turtle(user_turtle_start_position)

    def game_end(self):
        turtle.clearscreen()
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(OCEAN)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor='sw')

        self.update_score()

        self.current_world.obstacle_positions = []
        self.myrtle = RobotBird(
            colour='#402e08',
            shape='turtle',
            speed=1,
            game=self,
            start_position=self.current_world.portal_position
        )
        while True:
            self.myrtle.move()


turtle.listen()

game = Game()
game.create_base_world()
game.draw_world()

game.create_user_turtle((0, 0))

game.create_robot_bird()

while True:
    for bird in game.birds:
        bird.move()


turtle.mainloop()
