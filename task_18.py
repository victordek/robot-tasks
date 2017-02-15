#!/usr/bin/python3

from pyrob.api import *
import roborders as rd


@task
def task_8_28():
    rd.move_to_wall('right')
    rd.move_along_the_wall('left', 'up')
    if not wall_is_above():
        move_up()
    else:
        rd.move_along_the_wall('right', 'down')
        if not wall_is_beneath():
            move_down()

    # going to finish
    rd.move_to_wall('left')
    rd.move_to_wall('up')

if __name__ == '__main__':
    run_tasks()
