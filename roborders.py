#!/usr/bin/python3

from pyrob.api import *

def get_direct_functions (direct):
    '''Return move_direct and wall_condition for not smashing into the wall
    direct: ['right', 'leaft', 'up', 'down']'''
    if direct == 'right':
        return move_right, wall_is_on_the_right
    elif direct == 'left':
        return move_left, wall_is_on_the_left
    elif direct == 'up':
        return move_up, wall_is_above
    elif direct == 'down':
        return move_down, wall_is_beneath

def move_to_wall (direct = 'right'):
    '''Moving the robot in the given direction till the wall
	direct: ['right', 'leaft', 'up', 'down']'''
    move_direct, check_wall = get_direct_functions(direct)
    while not check_wall():
        move_direct()

def move_along_the_wall (direct, wall_on_the_side):
    '''Moving along the wall on the side in the given direction.
    Checking that wall is on the side than moving. So stops after the wall
    direct: ['right', 'leaft', 'up', 'down']
    wall_on_the_side: ['right', 'leaft', 'up', 'down']'''
    if direct == wall_on_the_side:
        print ("Direrctions shouldn`t be the same")
        return

    # move_direct contains function to move
    # check_move_direct contains checker of the direction
    if direct == 'right':
        check_move_direct = wall_is_on_the_right
        move_direct = move_right
    elif direct == 'left':
        check_move_direct = wall_is_on_the_left
        move_direct = move_left
    elif direct == 'up':
        check_move_direct = wall_is_above
        move_direct == move_up
    elif direct == 'down':
        check_move_direct = wall_is_beneath
        move_direct = move_down

    # check_side_wall contains the side to check the wall
    if wall_on_the_side == 'right':
        check_side_wall = wall_is_on_the_right
    elif wall_on_the_side == 'left':
        check_side_wall = wall_is_on_the_left
    elif wall_on_the_side == 'up':
        check_side_wall = wall_is_above
    elif wall_on_the_side == 'down':
        check_side_wall = wall_is_beneath

    while check_side_wall():
        if not check_move_direct():
            move_direct()
        else:
            # stop function and prevent smashing in to the corner
            return

