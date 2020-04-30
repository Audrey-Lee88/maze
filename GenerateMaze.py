from random import shuffle, randrange, choice


def make_maze(w, h):
    vis = [['0'] * w + ['1'] for _ in range(h)] + [['1'] * (w + 1)]
    ver = [["0"] * (w - 1) + ['0'] for _ in range(h)] + [[]]
    hor = [["0"] * (w - 1) + ['0'] for _ in range(h)]

    def walk(x, y):
        vis[y][x] = "1"

        neigh = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(neigh)
        for (dx, dy) in neigh:
            if vis[dy][dx] == "1":
                continue
            if dx == x:
                hor[max(y, dy)][x] = "1"
            if dy == y:
                ver[y][max(x, dx)] = "1"
            walk(dx, dy)

    walk(randrange(w), randrange(h))

    s = []
    for (a, b) in zip(hor, ver):
        s.append(min(a,b))
    return s



if __name__ == '__main__':
    print(make_maze(5, 5))