from BreadthFirstSearch import start


class PledgeAlgorithm:
    def __init__(self):
        self.maze_dict = dict()

    def end(self, maze, moves, begin):
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
            print(moves)
            print(self.maze_dict)
            return True

        return False


    def check(self, maze, moves, begin):
        i = begin
        j = 0
        track = []
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
            if self.maze_dict[(j, i)] is False:
                track.append(move)

            self.maze_dict[(j, i)] = True

        print(self.maze_dict)
        if track == []:
            return False

        return True


    def pledge(self, m):
        # create a dictionary to tag each index as visited or unvisited
        for i in range(len(m)):
            for j in range(len(m[0])):
                self.maze_dict[(i, j)] = False
        moves = ["S", "W", "E", "N"]
        # n = len(moves) -1
        begin = start(m)
        move = "None"
        for i in moves:
            if self.check(m, i, begin):
                move = i
                break
        past_moves = [move]
        if move == "None":
            return False

        counter = 1
        print(counter)
        while counter != 0:
            if self.end(m, past_moves, begin):
                print('end')
                break

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

            if self.check(m, temp0, begin):
                print("you go forward")
                past_moves.append(moves[0])
                counter = 1

            elif not self.check(m, temp0, begin):
                print("elif")
                if self.check(m, temp1, begin):
                    print("you turn right")
                    past_moves.append(moves[1])
                    counter += 90
                    print(counter)

                elif not self.check(m, temp1, begin):

                    if self.check(m, temp2, begin):
                        print("you turn left")
                        past_moves.append(moves[2])
                        counter += 270
                        print(counter)

                    elif self.check(m, temp3, begin):
                        print("turn around")
                        past_moves.append(moves[3])
                        counter += 180
                        print(counter)

                    else:
                        print("you turn back")
                        past_moves.append(moves[0])
                        print(past_moves)

        return True

if __name__ == "__main__":
    m = [['1', '1', 's', '0', '1'],
         ['1', '1', '1', '1', '1'],
         ['1', '1', '1', '1', '1'],
         ['1', 'e', '1', '1', '1']]
    P = PledgeAlgorithm()
    P.pledge(m)