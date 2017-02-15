#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_2_2():
    move_down()
    rd.draw_cross()
    for i in range (4):
        move_right(4)
        rd.draw_cross()


if __name__ == '__main__':
    run_tasks()
