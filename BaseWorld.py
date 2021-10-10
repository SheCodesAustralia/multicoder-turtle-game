import turtle
# import tkinter


def create_base_world():
    # turtle.setup(520, 520)
    screen = turtle.Screen()
    screen.setup(520, 520)
    screen.setworldcoordinates(0, 0, 500, 500)
    screen.bgpic('grid-white.gif')
    screen.bgcolor('pink')

    canvas = screen.getcanvas()
    canvas.itemconfig(screen._bgpic, anchor="sw")

    ##
    # photoimage = screen._bgpics['grid-white.gif']
    # pw = photoimage.width()
    # ph = photoimage.height()

    # canvas = screen.getcanvas()
    # canvas.configure(borderwidth=0)
    # screen.screensize(pw-100, ph-100)
    # screen.bgpic('grid-white.gif')
    ##

    # screen.bgcolor('red')
    return screen


# from turtle import Turtle, Screen

# screen = Screen()
# screen.setup(500, 500)
# screen.setworldcoordinates(0, 0, 500, 500)

# screen.bgpic("cat.gif")
# canvas = screen.getcanvas()
# canvas.itemconfig(screen._bgpic, anchor="sw")  # pylint: disable=W0212

# turtle = Turtle()
# turtle.dot(100)  # draw a large dot at (0, 0)

# screen.mainloop()
