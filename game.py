# superclass for world settings
#   set it up like a grid
# subclass has a different style

# could flash turtle red when tries to move into an obstacle
import turtle
from Turtle import CustomTurtle
from World import World
from config import STEP_SIZE


class Game:

    def __init__(self):
        self.create_base_world()

    def create_turtle(self):
        return CustomTurtle('blue', 2) 

    def create_base_world(self):
        screen = turtle.Screen()
        screen.setup(520, 520)
        screen.setworldcoordinates(0, 0, 500, 500)
        screen.bgpic('grid-white.gif')
        screen.bgcolor('pink')

        canvas = screen.getcanvas()
        canvas.itemconfig(screen._bgpic, anchor="sw")


game = Game()
world = World()
world.draw_obstacles()
myrtle = game.create_turtle()
myrtle.goto(STEP_SIZE/2, STEP_SIZE/2)
turtle.listen()

turtle.onkey(myrtle.move_forward, 'Up')
turtle.onkey(myrtle.move_backward, 'Down')
turtle.onkey(myrtle.turn_left, 'Left')
turtle.onkey(myrtle.turn_right, 'Right')


turtle.mainloop()
