# Winwin
# Author: Iris Wong

from turtle import right, forward, penup, pendown, hideturtle
from figure import draw_figure, set_initial_position
from letters import winwin_letters
from helpers import no_delay, setup
from settings import SIZEFACTOR, SHIRT_COLOR, START_X, START_Y

def main():
    hideturtle()
    setup(START_X,START_Y)

    with no_delay():
        #draw figure
        set_initial_position(SIZEFACTOR)
        draw_figure(SIZEFACTOR, SHIRT_COLOR)

        #moving to the letters
        penup()
        forward(50 * SIZEFACTOR)
        pendown()

        #draw letters
        winwin_letters(SIZEFACTOR)
        input("Press enter...")


if __name__ == '__main__':
    main()
