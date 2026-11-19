"""
Project 3 - Spinning Squares

Draws 90 squares, turning 4 degrees before each one,
so together they make a round pattern (90 x 4 = 360 degrees).
"""

from turtle import *

bob = Turtle('turtle')
bob.hideturtle()
bob.speed(0)

for _ in range(90):
    bob.right(4)
    for _ in range(4):
        bob.forward(100)
        bob.right(90)

done()