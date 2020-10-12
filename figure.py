# letter i code from homework_04
from turtle import forward, backward, left, right, circle, penup, pendown, pensize, pencolor, speed, goto, fillcolor, begin_fill, end_fill
from turtle import right, forward, penup, pendown
import settings

def set_initial_position(sf):
    penup()
    right(90)
    forward(50 * sf)
    right(90)
    forward(170 * sf)
    right(110)
    pendown()

def draw_figure(sf):
#draw shirt
    #color fill shirt
    fillcolor(settings.shirt_color)
    begin_fill()

    #shirt left rise
    for i in range(7):
        forward(5 * sf)
        right(1)
    for i in range(5):
        forward(5 * sf)
        right(6)

    #shirt collar line
    right(75)
    forward(20 * sf)
    for i in range(4):
        forward(5 * sf)
        right(350)
    right(340)
    forward(5 * sf)

    #shirt right descent
    right(83)
    for i in range(6):
        forward(5 * sf)
        right(2)
    forward(2 * sf)
    end_fill()

    #moving to neck starting point
    penup()
    right(92)
    forward(72 * sf)
    right(110)
    #shirt left rise
    for i in range(7):
        forward(5 * sf)
        right(1)
    for i in range(5):
        forward(5 * sf)
        right(6)
    forward(9 * sf)
    pendown()

#draw neck
    #left neckline
    right(350)
    forward(15 * sf)

    #neck turn
    for i in range(4):
        forward(2.5 * sf)
        right(325)

#draw hair
    #color fill hair
    fillcolor("black")
    begin_fill()

    #neck line underneath
    right(45)
    for i in range(3):
       forward(6 * sf)
       left(10)

    #hair zigzag
    left(45)
    forward(5 * sf)
    right(110)
    forward(15 * sf)

    #head left curve
    circle(-40 * sf, 40)
    for i in range(4):
        forward(2.5 * sf)
        right(10)

    #two lines and zigzag
    forward(15 * sf)
    right(45)
    forward(5 * sf)
    left(90)
    forward(5 * sf)
    right(40)

    #head right curve
    for i in range(6):
        forward(9 * sf)
        right(15)
    for i in range(2):
        forward(10 * sf)
        right(25)

    #hair zigzag bottom
    right(48)
    forward(25 * sf)
    left(65)
    forward(15 * sf)
    right(125)
    forward(25 * sf)
    left(55)

    #hair bottom curve complete
    for i in range(4):
        forward(2.5 * sf)
        left(20)
    for i in range(4):
        forward(5 * sf)
        left(4)

    #hair bottom line complete
    right(90)
    forward(12 * sf)
    end_fill()

    #moving to the forehead starting point
    penup()
    right(168)
    forward(69 * sf)
    right(140)
    pendown()

#draw facial features
    #forehead
    forward(6 * sf)
    for i in range(4):
        forward(1 * sf)
        left(15)
    right(15)

    #nose
    forward(12 * sf)
    for i in range(3):
        forward(1.5 * sf)
        right(30)
    forward(5 * sf)

    #upper lip
    left(85)
    forward(2 * sf)
    for i in range(2):
        forward(2 * sf)
        right(30)
    forward(3 * sf)

    #lower lip
    left(90)
    forward(1 * sf)
    circle(-2 * sf, 100)

    #chin
    for i in range(3):
        forward(2 * sf)
        left(30)
    right(30)
    for i in range(3):
        forward(2 * sf)
        right(35)
    left(20)
    forward(10 * sf)

    #right neckline
    circle(35 * sf, 30)
    forward(2 * sf)
    left(20)
    forward(5 * sf)
    right(24)
    forward(19.5 * sf)

    #moving to the ear starting point
    penup()
    right(135)
    forward(73 * sf)
    left(100)
    pendown()

    #ear
    for i in range(4):
        forward(2 * sf)
        left(20)
    for i in range(2):
        forward(4 * sf)
        left(10)
    for i in range(6):
        forward(2 * sf)
        left(10)
    for i in range(2):
        forward(4 * sf)
        left(10)
