from random import shuffle, randrange


def make_maze(w=5, h=5):
    vis = [[0] * (w) + [1] for _ in range(h)] + [[1] * (w+1)]
    ver = [["0"] * (w-1) + ['0'] for _ in range(h)] + [[]]
    hor = [["0"] * (w-1) + ['0'] for _ in range(h)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "1"
            if yy == y:
                ver[y][max(x, xx)] = "1"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = []
    for (a, b) in zip(hor, ver):
        s.append(min(a,b))
    return s


if __name__ == '__main__':
    print(make_maze())