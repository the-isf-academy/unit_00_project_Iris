# Winwin
# Author: Iris Wong

from turtle import right, forward, penup, pendown, hideturtle
from figure import draw_figure, set_initial_position
from letters import winwin_letters
from helpers import no_delay
import settings

size_factor = settings.sf


def main():
    hideturtle()
    with no_delay():
        #draw figure
        set_initial_position(size_factor)
        draw_figure(size_factor)

        #moving to the letters
        penup()
        forward(50 * size_factor)
        pendown()

        #draw letters
        winwin_letters(size_factor)
        input("Press enter...")


if __name__ == '__main__':
    main()
