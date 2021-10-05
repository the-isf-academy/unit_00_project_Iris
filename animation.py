import time
from turtle import *
from helpers import no_delay, restore_state_when_finished, setup
from figure import draw_figure, set_initial_position
from letters import letter_i, letter_n, letter_w
import settings

def draw_stationary(sf, shirt_color):
    with no_delay():
        set_initial_position(sf)
        draw_figure(sf, shirt_color)
        penup()
        forward(50 * sf)
        pendown()

def draw_animation(num_frames, sf, sleeptime):
    for i in range(num_frames):
        if (i == 10):
            letter_w(sf)
        if (i == 20):
            letter_i(sf)
        if (i == 30):
            letter_n(sf)
        if (i == 40):
            letter_w(sf)
        if (i == 50):
            letter_i(sf)
        if (i == 60):
            letter_n(sf)
        screen.update()
        time.sleep(sleeptime)
    clear()

def main():
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_stationary(settings.SIZEFACTOR, settings.SHIRT_COLOR)
        draw_animation(settings.NUMFRAMES, settings.SIZEFACTOR, settings.SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(800,800)
    main()
