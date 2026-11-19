"""
Project 1 - Square

A blue turtle draws a square by moving forward
and turning right, four times.
"""

from turtle import *

bob = Turtle('turtle')
bob.color('blue')
bob.turtlesize(2)

for _ in range(4):
    bob.forward(100)
    bob.right(90)

done()