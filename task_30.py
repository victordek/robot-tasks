#!/usr/bin/python3

from pyrob.api import *
import roborders as rd



@task(delay=0.01)
def task_9_3():
    # count the length
    length = 1
    while not wall_is_on_the_right():
        move_right()
        length += 1

    rd.draw_triangle(length, 'down', 'left')
    rd.draw_triangle(length, 'left', 'down')
    rd.move_to_the_opposite_corner()
    rd.draw_triangle(length, 'up', 'right')
    rd.draw_triangle(length, 'right', 'up')


if __name__ == '__main__':
    run_tasks()
