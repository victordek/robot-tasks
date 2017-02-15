#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_5_10():
    while not wall_is_beneath():
        rd.filling_the_line_from_end_to_end('right')
        move_down()
    rd.filling_the_line_from_end_to_end('right')

if __name__ == '__main__':
    run_tasks()
