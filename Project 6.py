"""
Project 6 - Arrow Key Turtle

Move a blue circle around the screen with the arrow keys.
It stops at the edges of the window so it can't go off screen.
"""

from turtle import *

STEP = 10
LIMIT = 190

# Set up the screen
screen = Screen()
screen.setup(width=410, height=410)
screen.screensize(canvwidth=360, canvheight=360)
screen.bgcolor('tan')
screen.title('Arrow Key Turtle')

# Set up the round turtle
bob = Turtle('circle')
bob.color('blue')
bob.penup()
bob.speed(0)


# Each function moves the turtle one step,
# but only if it won't go past the edge of the screen.
# round() fixes tiny math errors, like 189.99999 instead of 190
def go_up():
    """Face up and take one step, if not at the top edge."""
    bob.setheading(90)
    print(bob.xcor(), bob.ycor())
    if round(bob.ycor()) < LIMIT:
        bob.forward(STEP)


def go_down():
    """Face down and take one step, if not at the bottom edge."""
    bob.setheading(270)
    print(bob.xcor(), bob.ycor())
    if round(bob.ycor()) > -LIMIT:
        bob.forward(STEP)


def go_left():
    """Face left and take one step, if not at the left edge."""
    bob.setheading(180)
    print(bob.xcor(), bob.ycor())
    if round(bob.xcor()) > -LIMIT:
        bob.forward(STEP)


def go_right():
    """Face right and take one step, if not at the right edge."""
    bob.setheading(0)
    print(bob.xcor(), bob.ycor())
    if round(bob.xcor()) < LIMIT:
        bob.forward(STEP)


# Tell the screen which function to call for each arrow key
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.listen()

done()
