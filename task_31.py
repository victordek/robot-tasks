#!/usr/bin/python3

from pyrob.api import *
import roborders as rd



@task(delay=0.01)
def task_8_30():
    while True:
        rd.move_to_wall('right')
        rd.move_along_the_wall('left', 'down')
        if not wall_is_beneath():
            rd.move_to_wall('down')
            continue
        else:
            return


if __name__ == '__main__':
    run_tasks()
