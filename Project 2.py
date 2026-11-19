"""
Project 2 - Rainbow Square

A turtle draws a square where each side
is a different color.
"""

from turtle import *

COLORS = 'red', 'orange', 'green', 'blue'

bob = Turtle('turtle')
bob.color('violet')
bob.turtlesize(2)
bob.pensize(3)

for i in range(4):
    bob.pencolor(COLORS[i])
    bob.forward(100)
    bob.right(90)

done()