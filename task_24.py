#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_2_1():
    move_down()
    move_right()
    rd.draw_cross()


if __name__ == '__main__':
    run_tasks()
