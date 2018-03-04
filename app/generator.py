"""Generate a maze with a random solution."""
from random import randrange, shuffle


def main(w=16, h=8):
    """Generate a maze."""
    visited = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    row = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    col = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        visited[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        
        shuffle(d)
        for (xx, yy) in d:
            if visited[yy][xx]:
                continue
            if xx == x:
                col[max(y, yy)][x] = "+  "
            if yy == y:
                row[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(col, row):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


if __name__ == '__main__':
    maze = main()
    print(maze)
