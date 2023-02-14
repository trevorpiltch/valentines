import turtle
import keyboard

paused = False

def pause():
    global paused
    paused = True
    pausing()


pen = turtle.Turtle()

pen.screen.onkeypress(pause) 
pen.screen.listen()             

index = 0

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def draw():
    global index

    if index % 3 == 0:
        pen.fillcolor('pink')
    else if index % 3 == 1:
        pen.fillcolor('yellow')
    else:
        pen.fillcolor('blue')
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

