"""
Project 10 - When Harry Met Sally

Two turtles, Harry and Sally, meet on a path in a park,
say hello in speech bubbles, and go their separate ways.
Click REPLAY to watch again, or QUIT to close the window.
"""

from turtle import *
import time

# Set up the screen.
# The screen goes from -200 to 200 left to right,
# and -200 to 200 bottom to top.
screen = Screen()
screen.setup(width=400, height=400)
screen.screensize(canvwidth=360, canvheight=360)
screen.bgcolor('green')
screen.title('When Harry Met Sally')

# Set up the drawing turtle
# (It is called painter, because turtle already has a command named pen)
painter = Turtle()
painter.hideturtle()
painter.penup()
painter.speed(0)

# Set up a separate turtle just for speech bubbles,
# so we can erase the bubbles without erasing the sky and grass
bubble_pen = Turtle()
bubble_pen.hideturtle()
bubble_pen.penup()
bubble_pen.speed(0)


def draw_rectangle(x, y, box_width, box_height, box_color):
    """Draw a filled rectangle.

    x and y locate the top-left corner.
    """
    painter.goto(x, y)
    painter.color(box_color)
    painter.setheading(0)
    painter.begin_fill()
    painter.forward(box_width)
    painter.right(90)
    painter.forward(box_height)
    painter.right(90)
    painter.forward(box_width)
    painter.right(90)
    painter.forward(box_height)
    painter.end_fill()


def speech_bubble(left_, bottom, box_width,
                  box_height, tail_x,  tip, words, font_size):
    """Draw a white speech bubble with a black outline, then write words.

    left_ and bottom are the bottom-left corner of the box.
    The pointy tail sticks down to (tail_x, tip), right above the speaker.
    """
    right_ = left_ + box_width
    top = bottom + box_height

    # Go around the bubble's edge: across the top, down the right side,
    # along the bottom (with a dip for the tail), and up the left side
    bubble_pen.color('black', 'white')
    bubble_pen.goto(left_, top)
    bubble_pen.pendown()
    bubble_pen.begin_fill()
    bubble_pen.goto(right_, top)
    bubble_pen.goto(right_, bottom)
    bubble_pen.goto(tail_x + 6, bottom)
    bubble_pen.goto(tail_x, tip)
    bubble_pen.goto(tail_x - 6, bottom)
    bubble_pen.goto(left_, bottom)
    bubble_pen.goto(left_, top)
    bubble_pen.end_fill()
    bubble_pen.penup()

    # Write the words in the middle of the bubble
    bubble_pen.goto(left_ + box_width / 2, bottom + 5)
    bubble_pen.write(words, align='center',
                     font=('Arial', font_size, 'bold'))


# Sky: the top half of the screen
# The screen is 400 tall, so half is 200
draw_rectangle(-200, 200, 400, 200, 'skyblue')

# Sun: a big yellow dot in the top-right part of the sky
# dot() draws a filled circle; 70 is how wide it is
painter.goto(110, 110)
painter.dot(70, 'yellow')

# The bottom half is already green grass from bgcolor

# Path: a gray stripe across the middle of the grass
# The grass goes from y = 0 down to y = -200, so its middle is y = -100
# The path is 40 tall, so its top is 20 above the middle
draw_rectangle(-200, -80, 400, 40, 'gray')

# REPLAY button in the lower-right corner of the screen
# It is a dark green box with white letters,
# from x = 95 to 175, and from y = -150 down to -180
# (dark green, so it doesn't blend into the green grass)
draw_rectangle(95, -150, 80, 30, 'darkgreen')
painter.color('white')
painter.goto(135, -173)
painter.write('REPLAY', align='center', font=('Arial', 12, 'bold'))

# QUIT button in the lower-left corner of the screen
# It is a red box with white letters,
# from x = -175 to -95, and from y = -150 down to -180
draw_rectangle(-175, -150, 80, 30, 'red')
painter.color('white')
painter.goto(-135, -173)
painter.write('QUIT', align='center', font=('Arial', 12, 'bold'))

# Small orange turtle
sally = Turtle('turtle')
sally.color('orange')
sally.shapesize(1)
sally.hideturtle()
sally.penup()

# Big purple turtle
harry = Turtle('turtle')
harry.color('purple')
harry.shapesize(2)
harry.hideturtle()
harry.penup()


def play():
    """Play the whole story from the beginning."""
    # Erase any speech bubbles left over from last time
    bubble_pen.clear()

    # Sally starts at the left edge of the path, facing right
    sally.hideturtle()
    sally.speed(0)
    sally.goto(-180, -100)
    sally.setheading(0)
    sally.showturtle()
    sally.speed(1)

    # Harry starts at the right edge of the path, facing left
    harry.hideturtle()
    harry.speed(0)
    harry.goto(180, -100)
    harry.setheading(180)
    harry.showturtle()
    harry.speed(1)

    # The turtles walk toward each other until they meet.
    # Sally is little and quick, so she takes big steps (10).
    # Harry is big and slow, so he takes small steps (5).
    # The gap is how far apart they are. When it gets down to 65,
    # they are close enough to say hello, so they stop.
    gap = harry.xcor() - sally.xcor()
    while gap > 65:
        sally.forward(10)
        harry.forward(5)
        gap = harry.xcor() - sally.xcor()

    # The turtles have met, so they say hello in speech bubbles!
    # Each bubble's tail points down at the turtle, wherever it ended up.
    # Harry's bubble is up high and Sally's is lower and to her left,
    # so the bubbles don't bump into each other.
    sally_x = sally.xcor()
    harry_x = harry.xcor()

    # Harry talks first
    speech_bubble(harry_x - 50, -40, 130, 36,
                  harry_x, -78, 'Hello, Sally', 16)

    # Wait 2 seconds
    time.sleep(2)

    # Then Sally answers
    speech_bubble(sally_x - 90, -76, 100, 30,
                  sally_x, -88, 'Hello, Harry', 12)

    # Wait 2 more seconds, then erase the speech bubbles
    time.sleep(2)
    bubble_pen.clear()

    # Sally steps down off the path to get out of Harry's way
    sally.setheading(270)
    sally.forward(35)
    sally.setheading(0)

    # Both keep walking until Sally is safely past Harry's tail
    while sally.xcor() < harry.xcor() + 40:
        sally.forward(10)
        harry.forward(5)

    # Sally steps back up onto the path
    sally.setheading(90)
    sally.forward(35)
    sally.setheading(0)

    # Just like in the movie, they go their separate ways.
    # They keep walking the same way they were going before they met.
    # Sally keeps going right and Harry keeps going left.
    # Harry walks until he is almost at the left end of the path.
    # Sally keeps walking even after she leaves the screen.
    # Each step takes time, so if she stopped, Harry would look like he sped up.
    while harry.xcor() > -150:
        sally.forward(10)
        harry.forward(5)

    # Harry turns around to look back at Sally for 2 seconds,
    # while Sally keeps on walking.
    # time.time() tells us what time it is right now, in seconds,
    # so we keep going until 2 seconds have passed since start_time.
    harry.setheading(0)
    start_time = time.time()
    while time.time() - start_time < 2:
        sally.forward(10)

    # Harry turns back the way he was going and walks off the screen.
    # Sally keeps walking too, so Harry stays at the same speed.
    harry.setheading(180)
    while harry.xcor() > -240:
        sally.forward(10)
        harry.forward(5)


def ignore_click(x, y):
    """Do nothing, so clicks are ignored while the story is playing."""


def screen_clicked(x, y):
    """Run whenever someone clicks on the screen.

    x and y are where they clicked.
    """
    # Only replay if the click was inside the REPLAY button
    if 95 < x < 175 and -150 > y > -180:
        # Stop listening for clicks while the story plays,
        # so clicking again in the middle doesn't mess it up
        screen.onclick(ignore_click)
        play()
        # The story is over, so start listening for clicks again
        screen.onclick(screen_clicked)

    # Close the window if the click was inside the QUIT button
    if -175 < x < -95 and -150 > y > -180:
        screen.bye()


# Play the story once, then wait for someone to click REPLAY or QUIT
play()
screen.onclick(screen_clicked)

done()
