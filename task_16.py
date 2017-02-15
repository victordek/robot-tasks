#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_8_22():
    rd.move_to_wall('up')
    if wall_is_on_the_left():
        rd.move_to_wall('right')
    else:
        rd.move_to_wall('left')

if __name__ == '__main__':
    run_tasks()
