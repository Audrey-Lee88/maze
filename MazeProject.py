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
from GenerateMaze import make_maze
import time


class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = self.blank_slate()
        #do init stuff for 2D arrays

    def blank_slate(self):
        #populate the Maze with 0s, which
        #indicate maze walls
        maze = [['1' for i in range(self.size[0])] for j in range(self.size[1])]
        return maze

    def random_start_end(self):
        self.start = [0,np.random.randint(0,self.size[0]-1)]
        self.end = [self.size[1]-1,np.random.randint(0,self.size[1]-1)]
        print(self.start,self.end)
        self.maze[self.start[0]][self.start[1]] = 's'
        self.maze[self.end[0]][self.end[1]] = 'e'

    def add_noise(self):
        for i in range(self.size[0]):
            # print('\ni: ', i)
            for j in range(self.size[1]):
                # print('\nj: ', j)
                if self.maze[i][j] == '0' or self.maze[i][j] == 0:
                    number = random.randrange(0,100,1)
                    if number <= 45:
                        self.maze[i][j] = '1'

    def add_path(self):
        #overwrite a random succesfull path from
        #the start to end
        # Audrey
        self.maze = make_maze(self.size[0],self.size[1])
        self.random_start_end()
        self.add_noise()



def navigate_maze1(maze, exitIndex):
    #TODO: sweep the graph to find the start and end (use find start from BFS)
    #fix edge cases
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



def navigate_maze2(m):
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

def run(m):
    t = time.time()

    try:
        navigate_maze2(m)
    except time.time()-t > 6:
        print('hello')
        return False
    return True

def test_func():
    #TODO:
    #for sizes 10-100
    # for 10 iterations
    #generate a random maze, check to make sure it has a path from start to end
    #if not, regenerate a random maze and check again until has a path
    #start timer
    #run nav1
    #when end is found, end timer and save time and size of maze in tuple and append
    #to nav1list
    #start timer, run nav2
    #when end is found, ender timer and save time and size of maze in tuple and append
    #tuple to nav2list
    #plot?
    nav1list = []
    nav2list = []
    for size in range(10, 101):
        print('yep')
        for iter in range(10):
            maze = Maze((size,size))
            maze.add_path()
            print(maze.maze)
            bool = run(maze.maze)
            print('this is so sad')
            while bool == False:
                print('this is so sad')
                maze.blank_slate()
                maze.add_path()
                bool = run(maze.maze)
            # t = time.time()
            # navigate_maze1()
            # time = time.time()-t
            # nav1list.append((size, time))
            #second test
            t = time.time()
            print(maze.maze)
            navigate_maze2(maze.maze)
            timey = time.time()-t
            nav2list.append((size, timey))
    return nav2list


if __name__== "__main__":
    # m = [['1', '0', '0', '0'],
    #      ['1', '1', '0', '0'],
    #      ['0', '1', '0', '0'],
    #      ['0', '1', '1', '1']]
    #
    # print(navigate_maze1(m, 33))
    #
    # # m = [['s', '0', '0', '0'],
    # #      ['1', '1', '0', '0'],
    # #      ['0', '1', '0', '0'],
    # #      ['0', '1', '1', 'e']]
    #
    # maze = Maze((5,5))
    # maze.add_path()
    # print(maze.maze)
    # navigate_maze2(maze.maze)
    print(test_func())
