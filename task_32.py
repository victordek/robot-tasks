#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

def travel_down_the_hall():
    count = 0
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            count += 1
        else:
            fill_cell()
    rd.move_to_wall('down')
    return count





@task(delay=0.01)
def task_8_18():
    count = 0
    
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
            #move_right()
        else:
            count += travel_down_the_hall()
            #move_right()
        move_right()
    mov('ax', count)


if __name__ == '__main__':
    run_tasks()
