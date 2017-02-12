#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_5_3():
    while not wall_is_beneath():
        move_right()
    rd.move_along_the_wall('right', 'down')


if __name__ == '__main__':
    run_tasks()
