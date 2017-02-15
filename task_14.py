#!/usr/bin/python3

from pyrob.api import *
def check_and_fill():
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()

    if not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()
    if wall_is_above() and wall_is_beneath():
        fill_cell()


@task
def task_8_11():
    check_and_fill()

    while not wall_is_on_the_right():
        move_right()
        check_and_fill()

if __name__ == '__main__':
    run_tasks()
