#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

def condition (wall1, wall2):
    return not wall1()

def action_func():
    move_up()
    rd.filling_the_line_from_end_to_end('up')


@task(delay=0.01)
def task_6_6():
    move_right()
    rd.action_in_the_hall(condition, action = action_func)

    rd.move_along_the_wall('left', 'down')


if __name__ == '__main__':
    run_tasks()
