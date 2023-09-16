import numpy as np
import matplotlib.pyplot as plt
import gc

gc.enable()

HEIGHT = 480
WIDTH = 640
RES = 10
LINE_COLOR = "red"

np.random.seed(30)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


def random_generator():
    # create a width/res , height/res grid and randomly fill it with 0 or 1
    grid = np.random.randint(2, size=(1 + int(WIDTH / RES), 1 + int(HEIGHT / RES)))
    return grid


def visualize_grid(grid):
    for i in range(grid.shape[0] - 1):
        for j in range(grid.shape[1] - 1):
            if grid[i][j] == 1:
                plt.plot(i * RES, j * RES, "o", color="black", markersize=1)
            else:
                plt.plot(i * RES, j * RES, "o", color="white", markersize=1)


def getState(a, b, c, d):
    return a * 8 + b * 4 + c * 2 + d


def draw_line(point_1, point_2):
    plt.plot([point_1.x, point_2.x], [point_1.y, point_2.y], color=LINE_COLOR, linewidth=1)


def draw_seperator_line(a, b, c, d, grid):
    a_val = grid[a.x // RES][a.y // RES]
    b_val = grid[b.x // RES][b.y // RES]
    c_val = grid[c.x // RES][c.y // RES]
    d_val = grid[d.x // RES][d.y // RES]
    state = getState(a_val, b_val, c_val, d_val)
    if state == 1 or state == 14:
        draw_line(a - Point(0, 0.5 * RES), d + Point(0.5 * RES, 0))
    elif state == 2 or state == 13:
        draw_line(b - Point(0, 0.5 * RES), c - Point(0.5 * RES, 0))
    elif state == 3 or state == 12:
        draw_line(a - Point(0, 0.5 * RES), b - Point(0, 0.5 * RES))
    elif state == 4 or state == 11:
        draw_line(a + Point(0.5 * RES, 0), b - Point(0, 0.5 * RES))
    elif state == 5:
        draw_line(a + Point(0.5 * RES, 0), a - Point(0, 0.5 * RES))
        draw_line(b - Point(0, 0.5 * RES), c - Point(0.5 * RES, 0))
    elif state == 6 or state == 9:
        draw_line(a + Point(0.5 * RES, 0), c - Point(0.5 * RES, 0))
    elif state == 7 or state == 8:
        draw_line(a + Point(0.5 * RES, 0), a - Point(0, 0.5 * RES))
    elif state == 10:
        draw_line(a + Point(0.5 * RES, 0), b - Point(0, 0.5 * RES))
        draw_line(a - Point(0, 0.5 * RES), d + Point(0.5 * RES, 0))
    elif state == 0 or state == 15:
        pass
    else:
        raise Exception(f"Invalid state {state}")


def main():
    random_grid = random_generator()
    visualize_grid(random_grid)

    # make the background of plt gray
    plt.gca().set_facecolor((0.6, 0.6, 0.6))
    # make the plot axis start at 0, 0
    plt.axis([0, WIDTH, 0, HEIGHT])

    for x in range(0, WIDTH, RES):
        for y in range(0, HEIGHT, RES):
            a = Point(x, y)
            b = Point(x + RES, y)
            c = Point(x + RES, y - RES)
            d = Point(x, y - RES)
            draw_seperator_line(a, b, c, d, random_grid)

    plt.show()


if __name__ == "__main__":
    main()
