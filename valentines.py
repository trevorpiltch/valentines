import turtle
import keyboard

paused = False

def unpause():
    print("unpause() called")
    global paused
    paused = False
    draw()

def pause():
    global paused
    paused = True
    pausing()  # Start watching for global to be changed.

def pausing():
    if paused:
        turtle.ontimer(pausing, 250)  # Check again after delay.

pen = turtle.Turtle()

pen.screen.onkeypress(pause)  # Reversed order of
pen.screen.listen()             # these two statements.

index = 0

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def draw():
    global index
    if index % 2 == 0:
        pen.fillcolor('pink')
    else:
        pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(130)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
    index += 1


while True:
    if not paused:
        draw()

