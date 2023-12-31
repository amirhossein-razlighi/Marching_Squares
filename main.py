import numpy as np
import matplotlib.pyplot as plt
import gc
from math import ceil

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

    def __mul__(self, other):
        if type(other) == Point:
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)


def random_generator(use_float=False):
    if not use_float:
        # create a width/res , height/res grid and randomly fill it with 0 or 1
        grid = np.random.randint(2, size=(1 + int(WIDTH / RES), 1 + int(HEIGHT / RES)))
        grid_values = None
    else:
        # create a width/res , height/res grid and randomly fill it with continuous values between -1 and 1
        grid = np.random.uniform(-1, 1, size=(1 + int(WIDTH / RES), 1 + int(HEIGHT / RES)))
        grid_values = 0.5 + grid / 2

    return grid, grid_values

def visualize_grid(grid, grid_values):
    if grid_values is None:
        grid_values = grid

    x_coords = np.arange(0, grid.shape[0] - 1, 1)
    y_coords = np.arange(0, grid.shape[1] - 1, 1)

    x_grid, y_grid = np.meshgrid(x_coords, y_coords)

    color_values = grid_values[x_grid, y_grid]

    plt.scatter(x_grid * RES, y_grid * RES, s=1, c=color_values, cmap='gray', marker='o')

def getState(a, b, c, d):
    return a * 8 + b * 4 + c * 2 + d


def draw_line(point_1, point_2):
    plt.plot([point_1.x, point_2.x], [point_1.y, point_2.y], color=LINE_COLOR, linewidth=1)

def linear_interpolation(point_1, point_2, a_val, b_val):
    t = (0.5 - a_val) / (b_val - a_val)

    return point_1 + (point_2 - point_1) * t


def draw_seperator_line(a, b, c, d, grid):
    a_val = grid[a.x // RES][a.y // RES]
    b_val = grid[b.x // RES][b.y // RES]
    c_val = grid[c.x // RES][c.y // RES]
    d_val = grid[d.x // RES][d.y // RES]

    state = getState(ceil(a_val), ceil(b_val), ceil(c_val), ceil(d_val))

    
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


def main(args):
    random_grid, grid_values = random_generator(use_float=args.use_float)
    visualize_grid(random_grid, grid_values)

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
    plt.savefig("test.png")
    plt.show()


if __name__ == "__main__":
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--use_float", type=bool, default=False)
    args = arg_parser.parse_args()
    main(args)
