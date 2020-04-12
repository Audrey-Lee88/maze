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
    def __init__(self, maze=[]):
        self.Maze = maze
        #do init stuff for 2D arrays

    def blank_slate(self):
        #populate the Maze with 0s, which
        #indicate maze walls
        pass

    def add_path(self):
        #overwrite a random succesfull path from
        #the start to end
        pass

    def add_noise(self):
        #add in extraneous 1s as to add unsuccesfull paths,
        #weight will have to be experimented with
        pass


def navigate_maze1():
    #Casey
    #depth first search (Trémaux's algorithm)
    pass

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

