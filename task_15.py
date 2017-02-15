#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_8_21():
    rd.move_to_the_opposite_corner()


if __name__ == '__main__':
    run_tasks()
