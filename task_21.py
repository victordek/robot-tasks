#!/usr/bin/python3

from pyrob.api import *
x_size = 13

@task(delay=0.05)
def task_4_11():
    move_down()
    for i in range(1, x_size + 1):

        for j in range(i):
            move_right()
            fill_cell()
        
        move_left(i)
        move_down()

    move_right()

if __name__ == '__main__':
    run_tasks()
