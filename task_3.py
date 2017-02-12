#!/usr/bin/python3

from pyrob.api import *
import roborders as rd

@task
def task_3_1():
    rd.move_to_wall

if __name__ == '__main__':
    run_tasks()
