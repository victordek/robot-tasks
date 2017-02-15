#!/usr/bin/python3

from pyrob.api import *

x_size = 27
y_size = 12

@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(y_size):
        
        for j in range(x_size):
            fill_cell()
            move_right()
        move_left(x_size)
        
        move_down()

if __name__ == '__main__':
    run_tasks()
