#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

def condition (wall_above, wall_beneath):
    return wall_above() != wall_beneath()

@task
def task_8_2():
    rd.action_in_the_hall(condition)

if __name__ == '__main__':
    run_tasks()
