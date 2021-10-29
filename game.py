import turtle
from Turtles import UserTurtle, RobotTurtle
from worlds import WORLDS
from config import ROCK, BIRD, OCEAN, GRID, UMBRELLA, FOOD


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
        self.screen.addshape(UMBRELLA)
        self.screen.addshape(FOOD)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")
        self.update_score()

    def draw_world(self):
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()
        self.current_world.draw_food()
    
    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f'Score: {self.score}', font=("Arial", 16, "normal"))

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

    def create_robot_turtle(self):
        bird = RobotTurtle(
            colour='#000000',
            shape='classic',
            speed=3,
            game=self,
            start_position=self.current_world.robot_start_position
        )
        bird.position = self.current_world.robot_start_position
        self.birds.append(bird)

    def find_next_world(self):
        self.clear_world()
        if (self.world == 2):
            self.game_end()
        else:
            user_turtle_start_position = self.current_world.portal_position
            self.score = self.score + 10
            self.update_score()
            self.world = self.world + 1
            self.current_world = WORLDS[self.world]
            self.draw_world()
            for count in range(self.world+1):
                self.create_robot_turtle()
            for bird in self.birds:
                bird.move()
            self.create_user_turtle(user_turtle_start_position)

    def game_end(self):
        turtle.clearscreen()
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(OCEAN)

        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor="sw")

        self.update_score()

        self.myrtle = RobotTurtle(
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

game.create_robot_turtle()

while True:
    for bird in game.birds:
        bird.move()


turtle.mainloop()
