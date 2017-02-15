#!/usr/bin/python3

from pyrob.api import *


def fil_or_not_fill (current, border):
    if current >= border :
        return 0, border + 1, True
    else:
        return current + 1, border, False

@task
def task_7_5():
    count = 0
    border = -1

    #move_right()
    while not wall_is_on_the_right():
        move_right()
        if wall_is_on_the_right():
            return
        count, border, decision = fil_or_not_fill (count, border)

        if decision:
            fill_cell()
        
        
        




if __name__ == '__main__':
    run_tasks()
