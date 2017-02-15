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
        #print (count, border)
        move_right()
        count, border, decision = fil_or_not_fill (count, border)
        if decision:
            fill_cell()
        #move_right()



if __name__ == '__main__':
    run_tasks()
