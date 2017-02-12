#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_5_4():
    #the boarder of the field
    rd.move_along_the_wall('down', 'left')
    #the wall
    rd.move_along_the_wall('right', 'down')
    #around the end of the wall
    move_down()
    move_left()
    #to the exit
    rd.move_along_the_wall('left', 'up')


if __name__ == '__main__':
    run_tasks()
