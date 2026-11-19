"""
Project 11 - My House

Draws a house built from turtle shapes.
Left-click the door to open it, right-click to close it.
Left-click a window to turn on the lights, right-click to turn them off.
"""

from turtle import *

screen = Screen()
screen.setup(500, 500)
screen.title("My House")
screen.bgcolor("tan")
screen.tracer(0)  # only redraw the screen when we say so

# main level of the house
first_level = Turtle('square')
first_level.color('brown')
first_level.shapesize(6, 16)

# door
door = Turtle('square')
door.color('red')
door.shapesize(4, 2)
door.penup()
door.setposition(0, -20)

# left window
window_left = Turtle('square')
window_left.color('black')
window_left.shapesize(2, 2)
window_left.penup()
window_left.setposition(-100, 0)

# right window
window_right = window_left.clone()
window_right.setposition(100, 0)

# roof
roof = Turtle('triangle')
roof.color('brown')
roof.shapesize(16, 8)
roof.penup()
roof.setheading(90)
roof.setposition(0, 108)


def door_open(x, y):
    """Open the door by turning it black."""
    door.color('black')
    screen.update()


def door_close(x, y):
    """Close the door by turning it red again."""
    door.color('red')
    screen.update()


def lights_on(x, y):
    """Turn on the lights by making both windows yellow."""
    window_left.color('yellow')
    window_right.color('yellow')
    screen.update()


def lights_off(x, y):
    """Turn off the lights by making both windows black."""
    window_left.color('black')
    window_right.color('black')
    screen.update()


# left-click to open the door
door.onclick(door_open)

# right-click to close the door
door.onclick(door_close, 3)

# left-click either window to turn on the lights
window_left.onclick(lights_on)
window_right.onclick(lights_on)

# right-click either window to turn off the lights
window_left.onclick(lights_off, 3)
window_right.onclick(lights_off, 3)

# instructions at the bottom of the screen
writer = Turtle()
writer.hideturtle()
writer.penup()

writer.setposition(0, -140)
writer.write("Left-click either window to turn on lights", align='center',
             font=('Arial', 14, 'normal'))

writer.setposition(0, -165)
writer.write("Right-click either window to turn off lights", align='center',
             font=('Arial', 14, 'normal'))

writer.setposition(0, -190)
writer.write("Left-click door to open", align='center',
             font=('Arial', 14, 'normal'))

writer.setposition(0, -215)
writer.write("Right-click door to close", align='center',
             font=('Arial', 14, 'normal'))

screen.update()

done()
