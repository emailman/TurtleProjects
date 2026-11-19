# Turtle Projects

A series of beginner Python projects using the built-in `turtle` module.
Each project builds on ideas from the ones before it, starting with a
simple square and working up to keyboard controls, animation, and
clickable scenes.

## How to Run

You only need Python 3. The `turtle` module comes with Python, so there is
nothing extra to install.

Open a project in PyCharm and click **Run**, or run it from a terminal
(the quotes are needed because the file names have spaces):

```
python "Project 1.py"
```

Close the turtle window to end a program.

## The Projects

The description of each project below is the same as the docstring at the
top of its file.

### Project 1 - Square
A blue turtle draws a square by moving forward and turning right, four
times.

**You learn:** making a `Turtle`, `forward()`, `right()`, and `for` loops.

### Project 2 - Rainbow Square
A turtle draws a square where each side is a different color.

**You learn:** tuples of colors, `pencolor()`, `pensize()`, and using the
loop number `i` to pick an item from a tuple.

### Project 3 - Spinning Squares
Draws 90 squares, turning 4 degrees before each one, so together they make
a round pattern (90 x 4 = 360 degrees).

**You learn:** loops inside loops, `speed(0)` for fast drawing, and
`hideturtle()`.

### Project 4 - Colorful Spinning Squares
Draws 90 squares, turning 4 degrees before each one. The squares cycle
through red, orange, green, and blue.

**You learn:** the `%` (remainder) operator to repeat through a list of
colors over and over.

### Project 5 - Custom Screen
Draws colorful spinning squares on a tan, custom-sized window. Each
square's number and color are printed in the console. If the window is
closed while drawing, the program exits without an error.

**You learn:** `Screen()`, `setup()`, `screensize()`, `title()`, and
`try` / `except` to handle errors.

### Project 6 - Arrow Key Turtle
Move a blue circle around the screen with the arrow keys. It stops at the
edges of the window so it can't go off screen.

**You learn:** writing functions, `screen.onkey()` and `screen.listen()`
for keyboard input, `if` checks, and `round()` to fix tiny math errors.

### Project 7 - Turtle in a Box
Move a blue circle with the arrow keys. Four brown walls make a box, and
the turtle stays inside it.

**You learn:** `stamp()` and `shapesize()` to draw rectangles, a
`draw_wall()` function with parameters, and using constants like `WALL`
and `THICK` so numbers are easy to change.

### Project 8 - Bouncing Ball
A red ball bounces around by itself inside four blue walls, drawing its
path as it goes. Try changing `speed_x` and `speed_y` to change how it
bounces!

**You learn:** animation with `screen.ontimer()`, `tracer(0)` and
`update()` for smooth movement, `global` variables, and reversing
direction to bounce.

### Project 9 - Smooth Arrow Key Turtle
Move a blue circle inside four brown walls with the arrow keys. The turtle
keeps moving while a key is held down, and stops when the key is let go.

**You learn:** `onkeypress()` (key pressed) vs. `onkey()` (key released),
and a game loop that runs over and over with `ontimer()`.

### Project 10 - When Harry Met Sally
Two turtles, Harry and Sally, meet on a path in a park, say hello in
speech bubbles, and go their separate ways. Click **REPLAY** to watch
again, or **QUIT** to close the window.

**You learn:** drawing filled shapes with `begin_fill()` / `end_fill()`,
`dot()`, writing text with `write()`, `while` loops, `time.sleep()` and
`time.time()`, using a separate turtle so drawings can be erased with
`clear()`, and clickable buttons with `screen.onclick()`.

### Project 11 - My House
Draws a house built from turtle shapes.

- Left-click the door to open it, right-click to close it.
- Left-click a window to turn on the lights, right-click to turn them off.

**You learn:** building pictures from stretched turtle shapes, `clone()`,
and clicking on a turtle itself with `turtle.onclick()` (button `3` is the
right mouse button).
