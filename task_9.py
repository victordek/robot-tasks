#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_2():
    #check the starting place for filling
    if wall_is_above() != wall_is_beneath():
        fill_cell()

    while not wall_is_on_the_right():
        move_right()
        # checking new position for filling
        if wall_is_above() != wall_is_beneath():
            fill_cell()


if __name__ == '__main__':
    run_tasks()
