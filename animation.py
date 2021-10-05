import time
from turtle import *
from helpers import no_delay, restore_state_when_finished, setup
from figure import draw_figure, set_initial_position
from letters import letter_i, letter_n, letter_w
from settings import SIZEFACTOR, SHIRT_COLOR, START_X, START_Y, NUMREPEATS, NUMFRAMES, SLEEPTIME

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
    for i in range(NUMREPEATS):
        setup(START_X,START_Y)
        draw_stationary(SIZEFACTOR, SHIRT_COLOR)
        draw_animation(NUMFRAMES, SIZEFACTOR, SLEEPTIME)
    input("Press enter...")

if __name__ == '__main__':
    screen = Screen()
    screen.setup(800,800)
    main()
