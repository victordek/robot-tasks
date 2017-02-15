#!/usr/bin/python3

from pyrob.api import *

# dictionary for the label based access to moving 
moving_functions = {
    'right': move_right,
    'left': move_left,
    'up': move_up,
    'down': move_down,
}
# dictionary for the label based access to wall checking
wall_functions = {
    'right': wall_is_on_the_right,
    'left': wall_is_on_the_left,
    'up': wall_is_above,
    'down': wall_is_beneath,
}

def move_to_wall (direct = 'right'):
    '''Moving the robot in the given direction till the wall
	direct: ['right', 'leaft', 'up', 'down']'''

    move_direct, wall_on_the_way = moving_functions[direct], wall_functions[direct]
    while not wall_on_the_way():
        move_direct()

def move_along_the_wall (direct, wall_on_side_direct):
    '''Moving along the wall on the side in the given direction.
    Checking that wall is on the side than moving. So stops in the next point from the wall`s end
    direct: ['right', 'leaft', 'up', 'down']
    wall_on_side_direct: ['right', 'leaft', 'up', 'down']'''
    
    if direct == wall_on_side_direct:
        print ("Direrctions shouldn`t be the same")
        return

    move_direct, wall_on_the_way = moving_functions[direct], wall_functions[direct]
    wall_on_the_side = wall_functions[wall_on_side_direct]

    while wall_on_the_side():
        if not wall_on_the_way():
            move_direct()
        else:
            # stop function and prevent smashing in to the corner
            return

def action_in_the_hall (condition, direct = 'right', side_wall1 = 'up', side_wall2 = 'down', action = fill_cell):
    '''Moving down the hall and applying action if condition is True. Condition is checked on each step.
    Both of side_wall could be calculated automaticly, but passing through parametres allos to control condition 
    condition: function with to params (2 side walls) to return True/False
    direct: ['right', 'leaft', 'up', 'down']
    side_wall1: ['right', 'leaft', 'up', 'down']
    side_wall2: ['right', 'leaft', 'up', 'down']
    action: anything'''

    move_direct, wall_on_the_way = moving_functions[direct], wall_functions[direct]
    wall_on_the_side1, wall_on_the_side2 = wall_functions[side_wall1], wall_functions[side_wall2]

    # checks starting position
    if condition(wall_on_the_side1, wall_on_the_side2):
        action()

    while not wall_on_the_way():
        move_direct()
        # checking new position for filling
        if condition(wall_on_the_side1, wall_on_the_side2):
            action()

def move_to_the_opposite_corner():
    '''Moving to the opposite corner of the field'''
    if wall_is_on_the_left():
        move_to_wall('right')
    else:
        move_to_wall('left')

    if wall_is_above():
        move_to_wall('down')
    else:
        move_to_wall('up')

