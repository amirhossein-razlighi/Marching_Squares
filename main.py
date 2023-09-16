import numpy as np
import matplotlib.pyplot as plt

HEIGHT = 480
WIDTH = 640
RES = 10

def random_generator():
  # create a width/res , height/res grid and randomly fill it with 0 or 1
  grid = np.random.randint(2, size=(int(WIDTH/RES), int(HEIGHT/RES)))
  return grid

def visualize_grid(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == 1:
                plt.plot(i * RES, j * RES, 'o', color='black', markersize=1)
            else:
                plt.plot(i * RES, j * RES, 'o', color='white', markersize=1)

def getState(a, b, c, d):
  return a*8 + b*4 + c*2 + d

def draw_line(point_1, point_2):
  plt.plot([point_1[0], point_2[0]], [point_1[1], point_2[1]], color='blue', linewidth=1)

def draw_seperator_line(figure, a, b, c, d, grid):
  a_val = grid[a[0] * RES][a[1] * RES]
  b_val = grid[b[0] * RES][b[1] * RES]
  c_val = grid[c[0] * RES][c[1] * RES]
  d_val = grid[d[0] * RES][d[1] * RES]
  state = getState(a_val, b_val, c_val, d_val)

if __name__ == '__main__':
  random_grid = random_generator()
  # show a HEIGHT x WIDTH grid with RES distance between nodes of the grid and random_grid values as colors of the nodes
  visualize_grid(random_grid)
  
  for x in range(0, WIDTH, RES):
    draw_line([x, 0], [x, RES])
  
  plt.show()