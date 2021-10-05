# Winwin
# Author: Iris Wong

from turtle import right, forward, penup, pendown, hideturtle
from figure import draw_figure, set_initial_position
from letters import winwin_letters
from helpers import no_delay, setup
import settings

def main():
    hideturtle()
    setup(settings.START_X,settings.START_Y)

    with no_delay():
        #draw figure
        set_initial_position(settings.SIZEFACTOR)
        draw_figure(settings.SIZEFACTOR, settings.SHIRT_COLOR)

        #moving to the letters
        penup()
        forward(50 * settings.SIZEFACTOR)
        pendown()

        #draw letters
        winwin_letters(settings.SIZEFACTOR)
        input("Press enter...")


if __name__ == '__main__':
    main()
