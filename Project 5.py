"""
Project 5 - Custom Screen

Draws colorful spinning squares on a tan, custom-sized window.
Each square's number and color are printed in the console.
If the window is closed while drawing, the program exits without an error.
"""

import sys
from tkinter import TclError
from turtle import *

COLORS = 'red', 'orange', 'green', 'blue', 'purple'

# Set up the screen
screen = Screen()
screen.setup(width=400, height=400)
screen.screensize(canvwidth=350, canvheight=350, bg='tan')
screen.title('Colored Squares')

# Set up the turtle
bob = Turtle('turtle')
bob.hideturtle()
bob.speed(0)
bob.pensize(2)

# Draw 90 squares, each offset by 4 degrees
# Exit if the window is closed while drawing
try:
    for rotate in range(90):
        bob.color(COLORS[rotate % len(COLORS)])
        print(rotate, COLORS[rotate % len(COLORS)])
        bob.right(4)
        for _ in range(4):
            bob.forward(100)
            bob.right(90)
    done()
except (Terminator, TclError):
    print('Window closed')
    sys.exit()