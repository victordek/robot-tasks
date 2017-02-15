#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_8_29():
    rd.move_to_wall('left')
    if not wall_is_above():
        rd.move_to_wall('up')
    else:
        rd.move_to_wall('right')
        if wall_is_above():
            # no way
            return
        else:
            rd.move_to_wall('up')
            rd.move_to_wall('left')

if __name__ == '__main__':
    run_tasks()
