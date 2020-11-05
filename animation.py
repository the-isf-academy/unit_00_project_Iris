import time
from turtle import *
from helpers import no_delay, restore_state_when_finished
from figure import draw_figure, set_initial_position
from letters import letter_i, letter_n, letter_w
import settings

screen = Screen()
screen.setup(800,800)

def setup(x, y):
    '''Sets up the turtle, ready to draw,
    at the given coordinates'''
    penup()
    goto(x, y)
    pendown()
    speed(0)
    hideturtle()
    tracer(0)
    setheading(0)

def draw_stationary():
    with no_delay():
        set_initial_position(settings.sf)
        draw_figure(settings.sf)
        penup()
        forward(50 * settings.sf)
        pendown()

def draw_animation():
    for i in range(70):
        if (i == 10):
            letter_w(settings.sf)
        if (i == 20):
            letter_i(settings.sf)
        if (i == 30):
            letter_n(settings.sf)
        if (i == 40):
            letter_w(settings.sf)
        if (i == 50):
            letter_i(settings.sf)
        if (i == 60):
            letter_n(settings.sf)
        screen.update()
        time.sleep(0.05)
    clear()

def main():
    for i in range(settings.loop_num):
        setup(0,0)
        draw_stationary()
        draw_animation()
    input("Press enter...")

if __name__ == '__main__':
    main()
