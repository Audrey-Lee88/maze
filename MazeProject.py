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
import matplotlib.pyplot as plt


class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = []
        #do init stuff for 2D arrays

    def blank_slate(self):
        #populate the Maze with 0s, which
        #indicate maze walls
        self.maze = [['0' for _ in range(self.size[0])] for _ in range(self.size[1])]

    def random_start_end(self):
        self.start = [0,np.random.randint(0,self.size[0]-1)]
        self.end = [self.size[1]-1,np.random.randint(0,self.size[1]-1)]
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
        self.blank_slate()
        self.maze = make_maze(self.size[0], self.size[1])
        self.random_start_end()
        self.add_noise()



def navigate_maze1(maze, second):
    #TODO: sweep the graph to find the start and end (use find start from BFS)
    #fix edge cases
    #Casey
    #depth first search (Trémaux's algorithm)
    y_index = 0
    x_index = 0
    maze_dict = {}
    stack = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'e':
                maze[i][j] = '1'
                exitIndex = (i,j)
            if maze[i][j] == 's':
                maze[i][j] = '1'
                tempVarI = i
                tempVarJ = j
                y_index = i
                x_index = j

    #create a dictionary to tag each index as visited or unvisited
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            maze_dict[(i,j)] = False
    #overwrite the exitIndex with the tag 'Exit'
    stack.append((y_index, x_index))
    while (y_index, x_index) != exitIndex:
        # print(stack)
        # print(second.maze)
        if len(stack) == 0:
            return False
        maze_dict[stack[-1]] = True
        stack = stack[0:-1]
        try:
            if maze[y_index + 1][x_index] == '1' and maze_dict[((y_index + 1),(x_index))] == False:
                stack.append(((y_index + 1),(x_index)))
        except IndexError:
            pass
        try:
            if maze[y_index][x_index + 1] == '1' and maze_dict[((y_index),(x_index + 1))] == False:
                stack.append(((y_index),(x_index + 1)))
        except IndexError:
            pass
        try:
            if y_index != 0:
                if maze[y_index - 1][x_index] == '1' and maze_dict[((y_index - 1),(x_index))] == False:
                    stack.append(((y_index - 1),(x_index)))
        except IndexError:
            pass
        try:
            if x_index != 0:
                if maze[y_index][x_index - 1] == '1' and maze_dict[((y_index),(x_index - 1))] == False:
                    stack.append(((y_index),(x_index - 1)))
        except IndexError:
            pass
        try:
            y_index = stack[-1][0]
            x_index = stack[-1][1]
        except IndexError:
            return False
    maze[exitIndex[0]][exitIndex[1]] = 'e'
    maze[tempVarI][tempVarJ] = 's'
    return True



def navigate_maze2(m):
    # Audrey
    # breadth first search
    # uses a queue to visit cells in increasing distance order from the start
    # until the finish is reached
    bfs(m)

def navigate_maze3():
    #pledge algorithm?
    #Audrey
    pass

def navigate_maze4(maze):
    #A* traversal
    stack = []
    x_index = 0
    y_index = 0
    maze_dict = {}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'e':
                maze[i][j] = '1'
                exitIndex = (i,j)
            if maze[i][j] == 's':
                maze[i][j] = '1'
                tempVarI = i
                tempVarJ = j
                y_index = i
                x_index = j

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            maze_dict[(i,j)] = (False)


    stack.append(((y_index, x_index), (len(maze)^2 + len(maze[0])^2)))
    while (y_index, x_index) != exitIndex:
        # print(stack)
        # print(second.maze)
        if len(stack) == 0:
            return False
        maze_dict[stack[0][0]] = True
        stack = stack[1:]

        try:
            if maze[y_index + 1][x_index] == '1' and maze_dict[((y_index + 1),(x_index))] == False:
                stack.append((((y_index + 1),(x_index)),((len(maze)-(y_index+1))^2 + (len(maze[0])-(x_index))^2)))
        except IndexError:
            pass
        try:
            if maze[y_index][x_index + 1] == '1' and maze_dict[((y_index),(x_index + 1))] == False:
                stack.append((((y_index),(x_index + 1)),((len(maze)-(y_index))^2 + (len(maze[0])-(x_index + 1))^2)))
        except IndexError:
            pass
        try:
            if y_index != 0:
                if maze[y_index - 1][x_index] == '1' and maze_dict[((y_index - 1),(x_index))] == False:
                    stack.append((((y_index - 1),(x_index)), ((len(maze)-(y_index-1))^2 + (len(maze[0])-(x_index))^2)))
        except IndexError:
            pass
        try:
            if x_index != 0:
                if maze[y_index][x_index - 1] == '1' and maze_dict[((y_index),(x_index - 1))] == False:
                    stack.append((((y_index),(x_index - 1)), ((len(maze)-(y_index))^2 + (len(maze[0])-(x_index-1))^2)))
        except IndexError:
            pass
        try:
            stack = sorted(stack, key=lambda x: x[1])
            y_index = stack[0][0][0]
            x_index = stack[0][0][1]
        except IndexError:
            return False
    maze[exitIndex[0]][exitIndex[1]] = 'e'
    maze[tempVarI][tempVarJ] = 's'
    return True




def run(m, second):
    if navigate_maze1(m, second):
        return True
    else:
        return False

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
    nav4list = []
    for size in range(5, 20):
        print(size, ' this is the size')
        maze = Maze((size,size))
        for iter in range(10):
            print('rep')
            maze.add_path()
            bool = run(maze.maze, maze)
            while bool == False:
                maze.maze = maze.blank_slate()
                maze.add_path()
                bool = run(maze.maze, maze)
            # t = time.time()
            # navigate_maze1()
            # time = time.time()-t
            # nav1list.append((size, time))
            #second test
            t = time.time()
            navigate_maze1(maze.maze, maze)
            timey = time.time()-t
            nav1list.append((size, timey))
            if size < 10:
                t = time.time()
                navigate_maze2(maze.maze)
                timey = time.time()-t
                nav2list.append((size, timey))
            else:
                nav2list.append((size, '5'))
            t = time.time()
            navigate_maze4(maze.maze)
            timey = time.time()-t
            nav4list.append((size, timey))
    return nav1list, nav2list, nav4list


if __name__== "__main__":
    m = [['s', '1', '1', '1'],
         ['1', '1', '0', '0'],
         ['0', '1', '0', '0'],
         ['1', '1', '1', 'e']]
    # #
    # print(navigate_maze1(m))
    #
    # m = [['s', '0', '0', '0'],
    #      ['1', '1', '0', '0'],
    #      ['0', '1', '0', '0'],
    #      ['0', '1', '1', 'e']]
    #
    # maze = Maze((5,5))
    # maze.add_path()
    # print(maze.maze)
    # print(maze.maze)
    # navigate_maze2(maze.maze)
    # print(navigate_maze4(maze.maze))
    nav1list, nav2list, nav4list = test_func()
    plt.scatter(*zip(*nav1list))
    plt.scatter(*zip(*nav2list))
    plt.scatter(*zip(*nav4list))
    plt.show()
