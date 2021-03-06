import queue
import time


def start(maze):
    # Find starting pos
    for x, pos in enumerate(maze[0]):
        if pos == "s":
            s = x
    return s


def valid(maze, moves, begin):
    i = begin
    j = 0
    for move in moves:
        # Move left, right, up, or down
        if move == "W":
            i -= 1
        elif move == "E":
            i += 1
        elif move == "N":
            j -= 1
        elif move == "S":
            j += 1

        # Check if in row length and column length
        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        # Check if not in wall
        elif maze[j][i] == "0":
            return False

    return True


def find_end(maze, moves, begin):
    i = begin
    j = 0
    for move in moves:
        if move == "W":
            i -= 1
        elif move == "E":
            i += 1
        elif move == "N":
            j -= 1
        elif move == "S":
            j += 1

    if maze[j][i] == "e":
        print("Shortest Path Directions: " + moves)
        return True

    return False


def bfs(maze):
    # Audrey
    # breadth first search
    # uses a queue to visit cells in increasing distance order from the start
    # until the finish is reached
    q = queue.Queue()
    q.put("")
    add = ""
    beg = start(maze)
    t = time.clock()
    while not find_end(maze, add, beg):
        add = q.get()
        # print(add)
        for j in ["N", "S", "E", "W"]:
            if time.clock()-t > 5:
                print('nope',time.clock()-t)
                return False
            push = add + j
            if valid(maze, push, beg):
                # print(push)
                q.put(push)

if __name__ == "__main__":

    m = [["0", "0", "1", "1", "0", "s", "0", "1", "1"],
        ["0", "1", "1", "1", "1", "1", "1", "1", "0"],
        ["0", "1", "1", "1", "1", "1", "0", "1", "1"],
        ["0", "1", "1", "1", "1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1", "1", "1", "0", "1"],
        ["1", "1", "0", "1", "1", "1", "1", "1", "1"],
        ["0", "1", "0", "1", "1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "1", "0", "1", "1", "e"]]

    for _ in range(10):
        bfs(m)
        t = time.clock()
        print(t)
