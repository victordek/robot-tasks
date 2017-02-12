#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_5_2():
    rd.move_along_the_wall('right', 'down')


if __name__ == '__main__':
    run_tasks()
