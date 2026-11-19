"""
Project 9 - Smooth Arrow Key Turtle

Move a blue circle inside four brown walls with the arrow keys.
The turtle keeps moving while a key is held down,
and stops when the key is let go.
"""

from turtle import *

STEP = 5
WALL = 150        # inside edge of the walls
THICK = 20        # how thick each wall is
LIMIT = WALL - 10 # the turtle is about 10 wide from its middle, so stop here

# Set up the screen
screen = Screen()
screen.setup(width=410, height=410)
screen.screensize(canvwidth=360, canvheight=360)
screen.bgcolor('tan')
screen.title('Arrow Key Turtle')
screen.tracer(0)  # only redraw the screen when we say so

# Set up a square turtle to stamp the walls
builder = Turtle('square')
builder.hideturtle()   # stamp() still works while hidden
builder.penup()
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

# How far the turtle moves each time.
# 0 means standing still, STEP means moving
step_size = 0


# Each of these points the turtle and starts it moving
def go_up():
    """Face up and start moving."""
    global step_size
    bob.setheading(90)
    step_size = STEP


def go_down():
    """Face down and start moving."""
    global step_size
    bob.setheading(270)
    step_size = STEP


def go_left():
    """Face left and start moving."""
    global step_size
    bob.setheading(180)
    step_size = STEP


def go_right():
    """Face right and start moving."""
    global step_size
    bob.setheading(0)
    step_size = STEP


def stop():
    """Stop the turtle when the arrow key is let go."""
    global step_size
    step_size = 0


def move():
    """Move the turtle, then keep it inside the walls.

    This runs over and over, every 20 milliseconds.
    """
    bob.forward(step_size)
    if bob.xcor() > LIMIT:
        bob.setx(LIMIT)
    if bob.xcor() < -LIMIT:
        bob.setx(-LIMIT)
    if bob.ycor() > LIMIT:
        bob.sety(LIMIT)
    if bob.ycor() < -LIMIT:
        bob.sety(-LIMIT)
    screen.update()  # redraw the screen
    screen.ontimer(move, 20)  # run move() again in 20 milliseconds


# Tell the screen which function to call
# when each arrow key is pressed and let go
screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')
screen.onkeypress(go_left, 'Left')
screen.onkeypress(go_right, 'Right')
screen.onkey(stop, 'Up')
screen.onkey(stop, 'Down')
screen.onkey(stop, 'Left')
screen.onkey(stop, 'Right')
screen.listen()

move()
done()
