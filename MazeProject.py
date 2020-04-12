#TODO:
#1A. Decide on what data structure our maze will be stored in.
#1B. Create a maze creation function (at some level of fidelity)
#2. Decide on what traversal strategies we will use
#3. Create ?3? traversal functions
#4. Create test functions that show completion times
#5. Plot comparisons between completion times

import numpy as np
import random
from BreadthFirstSearch import bfs


class Maze:
    def __init__(self, size):
        self.size = size
        #do init stuff for 2D arrays

    def blank_slate(self):
        #populate the Maze with 0s, which
        #indicate maze walls
        maze = [[0 for i in range(self.size[0])] for j in range(self.size[1])]
        print(maze)

    def add_path(self):
        #overwrite a random succesfull path from
        #the start to end
        # Audrey
        pass

    def add_noise(self):
        #add in extraneous 1s as to add unsuccesfull paths,
        #weight will have to be experimented with
        # Casey
        pass


def navigate_maze1(maze, exitIndex):
    #Casey
    #depth first search (Trémaux's algorithm)
    y_index = 0
    x_index = 0
    maze_dict = {}
    stack = []
    #create a dictionary to tag each index as visited or unvisited
    for i in range(len(m)):
        for j in range(len(m[i])):
            maze_dict[str(i) + str(j)] = False
    #overwrite the exitIndex with the tag 'Exit'
    maze_dict[str(exitIndex)] = 'Exit'
    print(maze_dict)
    stack.append('00')
    while maze_dict[str(y_index) + str(x_index)] != 'Exit':
        maze_dict[str(stack[-1][0]) + str(stack[-1][1])] = True
        print('Stack: ', stack)
        stack = stack[0:-1]
        print('X:', x_index, '\nY:', y_index)
        try:
            if maze[y_index + 1][x_index] == '1':
                stack.append(str(y_index + 1) + str(x_index))
        except IndexError:
            pass
        try:
            if maze[y_index][x_index + 1] == '1':
                stack.append(str(y_index) + str(x_index + 1))
        except IndexError:
            pass
        y_index = int(stack[-1][0])
        x_index = int(stack[-1][1])

    return maze_dict



def navigate_maze2(maze):
    # Audrey
    # breadth first search
    # uses a queue to visit cells in increasing distance order from the start
    # until the finish is reached
    bfs(m)

def navigate_maze3():
    #pledge algorithm?
    pass

def navigate_maze_control():
    #random mouse algorithm
    pass

if __name__== "__main__":
    m = [['1', '0', '0', '0'],
         ['1', '1', '0', '0'],
         ['0', '1', '0', '0'],
         ['0', '1', '1', '1']]
    # maze1 = Maze(maze=m)

    print(navigate_maze1(m, 33))
    m = [["x","x", "x", "x", "x", "s", "x", "x", "x"],
        ["x"," ", " ", " ", " ", " ", " ", " ", "x"],
        ["x"," ", " ", "x", "x", "x", "x", " ", "x"],
        ["x"," ", " ", " ", " ", " ", "x", " ", "x"],
        ["x"," ", "x", " ", " ", " ", "x", " ", "x"],
        ["x"," ", "x", " ", "x", " ", "x", " ", " "],
        ["x"," ", "x", " ", "x", " ", "x", "x", " "],
        ["e"," ", "x", " ", "x", " ", " ", " ", " "],
        ["x"," ", "x", " ", "x", " ", " ", " ", " "],
        ["x","x", "x", "x", "x", "x", "x", " ", "x"]]
    navigate_maze2(m)
    # maze1 = Maze(maze=m)
    maze = Maze((6, 6))
    maze.blank_slate()
