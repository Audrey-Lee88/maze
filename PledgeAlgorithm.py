from BreadthFirstSearch import valid, start


def end(maze, moves, begin):
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
        return True

    return False


def pledge(m):
    # create a dictionary to tag each index as visited or unvisited
    maze_dict = dict()
    for i in range(len(m)):
        for j in range(len(m[i])):
            maze_dict[(i, j)] = False
    moves = ["S", "W", "E", "N"]
    n = len(moves) -1
    begin = start(m)
    for i in moves:
        if valid(m, i, begin):
            move = i
    past_moves = [move]
    # i =1

    while not end(m, past_moves, begin):
        print(past_moves)
        # while i < 3:
        counter = 1
        print(counter)
        while counter != 0:
            if abs(counter)-1 == 0 or (abs(counter)-1)%360 == 0:
                print("zero")
                moves = ["S", "W", "E", "N"]
            elif (abs(counter)-1)%270 == 0:
                print("one")
                moves = ["E", "S", "N", "W"]
            elif (abs(counter)-1)%180 == 0:
                print("two")
                moves = ["N", "E", "W", "S"]
            elif (abs(counter)-1)%90  == 0:
                print('three')
                moves = ["W", "N", "S", "E"]

            print(counter, moves)
            temp0 = past_moves.copy()
            temp0.append(moves[0])
            print(temp0, past_moves,'temp')
            temp1 = past_moves.copy()
            temp1.append(moves[1])
            temp2 = past_moves.copy()
            temp2.append(moves[2])
            temp3 = past_moves.copy()
            temp3.append(moves[3])

            if valid(m, temp0, begin):
                print("you go forward")
                past_moves.append(moves[0])
                counter = 0

            elif not valid(m, temp0, begin):

                if valid(m, temp1, begin):
                    print("you turn right")
                    past_moves.append(moves[1])
                    counter += 90
                    print(counter)

                elif not valid(m, temp1, begin):

                    if valid(m, temp2, begin):
                        print("you turn left")
                        past_moves.append(moves[2])
                        counter += 270
                        print(counter)

                    else:
                        print("you turn back")
                        if end(m, past_moves, begin):
                            print('end')
                            break
                        past_moves.append(temp3)
                        print(past_moves)
                        break

        # i = 0
        # while i <= n:
        #     potential = past_moves +['N']
        #     print(potential)
        #     past_moves.append(moves[i])
        #     print(past_moves, 'past')
        #
        #     print(moves[i],"move")
        #
        #     if end(m, past_moves, begin) and valid(m, past_moves,begin):
        #         break
        #     if valid(m, potential, begin) and not valid(m, past_moves, begin):
        #         print("N",i)
        #
        #         past_moves.pop(-1)
        #         i += 1
        #         if i > n:
        #             print('shoot')
        #     elif valid(m, past_moves, begin):
        #         print(moves[i])
        #         i = 0
        #     else:
        #         i += 1
        #     potential.pop(-1)
        # counter = 1
        # print(counter)
        # while counter != 0:
        #     print(counter)
        #     if forward == "y":
        #         print("you go forward")
        #         past_move.append("forward")
        #
        #     elif forward == "n":
        #
        #         if right == "y":
        #             print("you turn right")
        #             past_move.append("right")
        #             counter += 89
        #             print(counter)
        #
        #         elif right == "n":
        #
        #             if left == "y":
        #                 print("you turn left")
        #                 past_move.append("left")
        #                 counter -= 91
        #                 print(counter)
        #
        #             else:
        #                 print("you turn back")
        #                 past_move.append("go back")


if __name__ == "__main__":
    m = [['0','0','s','1','1'],
         ['1','0','0','1','0'],
         ['0','0','1','1','e']]
    pledge(m)