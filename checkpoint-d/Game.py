import turtle
from Characters import UserTurtle, RobotBird
from World import World
from Obstacle import Obstacle
from utils import convert_coord_to_grid_pos
from worlds import WORLDS
from config import ROCK, BIRD, OCEAN, GRID, PORTAL, FOOD


class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.bird = None
        ##
        self.world = 0
        self.current_world = WORLDS[self.world]
        self.score = 0
        self.score_display = turtle.Turtle()
        ##

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
        ##
        self.update_score()
        ##

    def draw_world(self):
        ##
        self.current_world.draw_obstacles()
        self.current_world.draw_portal()
        ##
        pass
    
    def update_score(self):
        ##
        self.score_display.clear()
        self.score_display.write(f'Score: {self.score}', font=("Arial", 16, "normal"))
        ##
        pass
        
    def clear_world(self):
        ##
        turtle.clearscreen()
        self.create_base_world()
        ##
        pass

    def create_user_turtle(self, start_position):
        ##
        self.myrtle = UserTurtle(
            colour='#402e08',
            shape='turtle',
            speed=2,
            game=self,
            start_position=start_position
        )
        ##
        pass

    def create_robot_bird(self):
        ##
        bird = RobotBird(
            colour='#000000',
            shape='classic',
            speed=3,
            game=self,
            start_position=self.current_world.bird_start_position
        )
        self.bird = bird
        ##
        pass

    def find_next_world(self):
        ##
        self.clear_world()
        user_turtle_start_position = self.current_world.portal_position
        self.world = self.world + 1
        self.current_world = WORLDS[self.world]
        self.draw_world()
        self.create_robot_bird()
        self.bird.move()
        self.create_user_turtle(user_turtle_start_position)
        ##
        pass

    def game_end(self):
        ##
        # YOUR CODE HERE
        ##
        self.screen.setup(520, 520)
        self.screen.setworldcoordinates(0, 0, 500, 500)
        self.screen.bgpic(OCEAN)
        canvas = self.screen.getcanvas()
        canvas.itemconfig(self.screen._bgpic, anchor='sw')
        ##
        # YOUR CODE HERE
        ##


turtle.listen()

game = Game()
game.create_base_world()
game.draw_world()

##
game.create_user_turtle((0, 0))
game.create_robot_bird()

while True:
    game.bird.move()
##

turtle.mainloop()
