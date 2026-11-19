"""
Project 8 - Bouncing Ball

A red ball bounces around by itself inside four blue walls,
drawing its path as it goes.
Try changing speed_x and speed_y to change how it bounces!
"""

from turtle import *

WALL = 150        # inside edge of the walls
THICK = 20        # how thick each wall is
LIMIT = WALL - 10 # the ball is about 10 wide from its middle, so bounce here

# How far the ball moves each time (try changing these!)
speed_x = 4
speed_y = 3

# Set up the screen
screen = Screen()
screen.setup(width=410, height=410)
screen.screensize(canvwidth=360, canvheight=360)
screen.bgcolor('tan')
screen.title('Bouncing Ball')
screen.tracer(0)  # draw everything at once, so the ball moves smoothly

# Set up a square turtle to stamp the walls
builder = Turtle('square')
builder.hideturtle()   # stamp() still works while hidden
builder.penup()
builder.color('blue')


def draw_wall(x, y, wide, tall):
    """Stamp a blue rectangle centered at (x, y).

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

# Set up the ball
ball = Turtle('circle')
ball.color('red')
ball.pensize(2)
# ball.penup()


def move_ball():
    """Move the ball one step, and bounce if it reaches a wall."""
    global speed_x, speed_y

    x = ball.xcor() + speed_x
    y = ball.ycor() + speed_y

    # Bounce off the left or right wall
    if x > LIMIT:
        x = LIMIT
        speed_x = -speed_x
    if x < -LIMIT:
        x = -LIMIT
        speed_x = -speed_x

    # Bounce off the top or bottom wall
    if y > LIMIT:
        y = LIMIT
        speed_y = -speed_y
    if y < -LIMIT:
        y = -LIMIT
        speed_y = -speed_y

    ball.goto(x, y)
    screen.update()

    # Call move_ball again in 20 milliseconds
    screen.ontimer(move_ball, 20)


move_ball()

done()
