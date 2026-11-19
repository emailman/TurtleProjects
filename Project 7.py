"""
Project 7 - Turtle in a Box

Move a blue circle with the arrow keys.
Four brown walls make a box, and the turtle stays inside it.
"""

from turtle import *

STEP = 10
WALL = 150        # inside edge of the walls
THICK = 20        # how thick each wall is
LIMIT = WALL - 10 # the turtle is about 10 wide from its middle, so stop here

# Set up the screen
screen = Screen()
screen.setup(width=410, height=410)
screen.screensize(canvwidth=360, canvheight=360)
screen.bgcolor('tan')
screen.title('Turtle in a Box')

# Set up a square turtle to stamp the walls
builder = Turtle('square')
builder.hideturtle()   # stamp() still works while hidden
builder.penup()
builder.speed(0)
builder.color('brown')


def draw_wall(x, y, wide, tall):
    """Stamp a brown rectangle centered at (x, y).

    The square shape is 20 x 20, so we stretch it by size / 20.
    """
    builder.shapesize(tall / 20, wide / 20)
    builder.goto(x, y)
    builder.stamp()


# Draw the 4 walls
middle = WALL + THICK / 2      # center line of each wall (160)
outside = WALL + THICK         # outer edge of the walls (170)
draw_wall(0, middle, outside * 2, THICK)     # top wall
draw_wall(0, -middle, outside * 2, THICK)    # bottom wall
draw_wall(-middle, 0, THICK, WALL * 2)       # left wall
draw_wall(middle, 0, THICK, WALL * 2)        # right wall

# Set up the round turtle
bob = Turtle('circle')
bob.color('blue')
bob.penup()
bob.speed(0)


# Each function moves the turtle one step,
# but only if it won't go into a wall.
# round() fixes tiny math errors, like 139.99999 instead of 140
def go_up():
    """Face up and take one step, if not at the top wall."""
    bob.setheading(90)
    if round(bob.ycor()) < LIMIT:
        bob.forward(STEP)


def go_down():
    """Face down and take one step, if not at the bottom wall."""
    bob.setheading(270)
    if round(bob.ycor()) > -LIMIT:
        bob.forward(STEP)


def go_left():
    """Face left and take one step, if not at the left wall."""
    bob.setheading(180)
    if round(bob.xcor()) > -LIMIT:
        bob.forward(STEP)


def go_right():
    """Face right and take one step, if not at the right wall."""
    bob.setheading(0)
    if round(bob.xcor()) < LIMIT:
        bob.forward(STEP)


# Tell the screen which function to call for each arrow key
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.listen()

done()
