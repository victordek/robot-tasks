#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

def draw_line_of_crosses_and_back (number = 10):
    rd.draw_cross()
    for i in range(number - 1):
        move_right(4)
        rd.draw_cross()
    rd.move_to_wall('left')

@task(delay=0.02)
def task_2_4():
    draw_line_of_crosses_and_back()
    for i in range(4):
        move_down(4)
        draw_line_of_crosses_and_back()


if __name__ == '__main__':
    run_tasks()
