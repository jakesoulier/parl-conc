"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p1.py 
Author: <Add name here>

Purpose: Part 1 of assignment 09, finding a path to the end position in a maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included

"""
import math
from screen import Screen
from maze import Maze
import cv2
import sys

# Include cse 251 common Python files - Dont change
from cse251 import *

SCREEN_SIZE = 800
COLOR = (0, 0, 255)


# TODO add any functions

def solve_path(maze, path, row, col):
    """ Solve the maze and return the path found between the start and end positions.  
        The path is a list of positions, (x, y) """
        
    # start position
    if len(path) == 0:
        maze.move(row, col, (255, 0, 0))

    # base case
    if maze.at_end(row, col):
        print(f'You reached the end! {path=}')
        return True
    else:
        moves = maze.get_possible_moves(row, col)
        for move in moves:
            if maze.can_move_here(move[0], move[1]):
                maze.move(move[0], move[1], (255, 0, 0))
                path.append(move)
                if solve_path(maze, path, move[0], move[1]):
                    return path
                maze.restore(move[0], move[1])
                path.remove(move)

def get_path(log, filename):
    """ Do not change this function """

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename)
    give_path = []
    row = maze.start_pos[0]
    col = maze.start_pos[1]
    path = solve_path(maze, give_path, row, col)
    print(f'get_path {path=}')
    log.write(f'Number of drawing commands for = {screen.get_command_count()}')

    done = False
    speed = 1
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('+'):
                speed = max(0, speed - 1)
            elif key == ord('-'):
                speed += 1
            elif key != ord('p'):
                done = True
        else:
            done = True

    return path


def find_paths(log):
    """ Do not change this function """

    files = ('verysmall.bmp', 'verysmall-loops.bmp', 
            'small.bmp', 'small-loops.bmp', 
            'small-odd.bmp', 'small-open.bmp', 'large.bmp', 'large-loops.bmp')

    log.write('*' * 40)
    log.write('Part 1')
    count = 0
    for filename in files:
        log.write()
        log.write(f'File: {filename}')
        path = get_path(log, filename)
        print(f'path {path}, count {count}')
        count += 1
        log.write(f'Found path has length          = {len(path)}')
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_paths(log)


if __name__ == "__main__":
    main()