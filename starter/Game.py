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
        self.current_world = World(
            obstacle_positions=[],
            portal_position=(0, 1),
            bird_start_position=(0, 2),
            food_position=(0, 3)
        )
        self.bird = None
        ##
        # YOUR CODE HERE
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
        # YOUR CODE HERE
        ##

    def draw_world(self):
        ##
        # YOUR CODE HERE
        ##
        pass
    
    def update_score(self):
        ##
        # YOUR CODE HERE
        ##
        pass
        
    def clear_world(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def create_user_turtle(self, start_position):
        ##
        # YOUR CODE HERE
        ##
        pass

    def create_robot_bird(self):
        ##
        # YOUR CODE HERE
        ##
        pass

    def find_next_world(self):
        ##
        # YOUR CODE HERE
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
# YOUR CODE HERE
##

turtle.mainloop()
