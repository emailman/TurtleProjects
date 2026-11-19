"""
Project 4 - Colorful Spinning Squares

Draws 90 squares, turning 4 degrees before each one.
The squares cycle through red, orange, green, and blue.
"""

from turtle import *

COLORS = 'red', 'orange', 'green', 'blue'

bob = Turtle('turtle')
bob.hideturtle()
bob.speed(0)
bob.pensize(2)

for rotate in range(90):
    bob.color(COLORS[rotate % len(COLORS)])
    bob.right(4)
    for _ in range(4):
        bob.forward(100)
        bob.right(90)

done()