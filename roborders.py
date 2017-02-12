#!/usr/bin/python3

from pyrob.api import *

def move_to_wall (direct = 'right'):
    '''Moving the robot in the given direction till the wall
	direct: ['right', 'leaft', 'up', 'down']'''
    if direct == 'right':
        while not wall_is_on_the_right():
            move_right()
    elif direct == 'left':
        while not wall_is_on_the_left():
            move_left()
    elif direct == 'up':
        while not wall_is_above():
            move_up()
    elif direct == 'down':
        while not wall_is_beneath():
            move_down()