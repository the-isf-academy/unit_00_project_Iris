from turtle import forward, backward, right, circle, penup, pendown, speed, fillcolor, begin_fill, end_fill

def letter_w(sf):
    "Draws letter w"
    #color fill letter w
    fillcolor("#B3B7D2")
    begin_fill()

    #outer shell of w
    right(80)
    forward(25 * sf)
    right(280)
    forward(7.5 * sf)
    right(300)
    forward(7.5 * sf)
    right(120)
    forward(7.5 * sf)
    right(300)
    forward(7.5 * sf)
    right(280)
    forward(25 * sf)

    #inner shell of w
    right(260)
    forward(7.5 * sf)
    right(280)
    forward(15 * sf)
    right(140)
    forward(11 * sf)
    right(240)
    forward(11 * sf)
    right(140)
    forward(15 * sf)
    right(280)
    forward(7.5 * sf)
    right(180)
    end_fill()

    #placement for letter i
    penup()
    forward(35 * sf)
    pendown()


def letter_i(sf):
    #color fill letter i
    fillcolor("#CBACCC")
    begin_fill()

    #letter i
    for i in range(2):
        forward(7.5 * sf)
        right(90)
        forward(25 * sf)
        right(90)
    end_fill()

    #placement for letter n
    penup()
    forward(12.5 * sf)
    pendown()


def letter_n(sf):
    "Draws letter n"
    #color fill letter n
    fillcolor("#D7AAC0")
    begin_fill()

    #letter n
    for i in range(2):
        forward(10 * sf)
        right(70)
        forward(15 * sf)
        right(200)
        forward(14 * sf)
        right(90)
        forward(7.5 * sf)
        right(90)
        forward(25 * sf)
        right(90)
    end_fill()

    #placement for letter w
    penup()
    forward(26 * sf)
    pendown()

def winwin_letters(sf):
    for i in range(2):
        letter_w(sf)
        letter_i(sf)
        letter_n(sf)
