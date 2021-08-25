from torch import (roll, zeros)
import numpy as np
from timeit import timeit

grid_shape = (640, 640)


# ------------------------------------------------
def laplacian_np(grid):
    return (np.roll(grid, +1, 0)
            + np.roll(grid, -1, 0)
            + np.roll(grid, +1, 1)
            + np.roll(grid, -1, 1)
            - 4 * grid)


# ------------------------------------------------
def evolve_np(grid, dt, D=1):
    return grid + dt * D * laplacian_np(grid)


# ------------------------------------------------
def run_experiment_np(num_iterations=1000):
    grid = np.zeros(grid_shape)
    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    for i in range(num_iterations):
        grid = evolve_np(grid, 0.1)
    return grid


# ------------------------------------------------
def laplacian(grid):
    return (roll(grid, +1, 0)
            + roll(grid, -1, 0)
            + roll(grid, +1, 1)
            + roll(grid, -1, 1)
            - 4 * grid)


# ------------------------------------------------
def evolve(grid, dt, D=1):
    return grid + dt * D * laplacian(grid)


# ------------------------------------------------
def run_experiment(num_iterations=1000):
    grid = zeros(grid_shape)
    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    grid = grid.cuda()
    for i in range(num_iterations):
        grid = evolve(grid, 0.1)
    return grid


# ------------------------------------------------
if __name__ == '__main__':
    print(timeit(run_experiment_np, number=1))  # 10.1878083
    print(timeit(run_experiment, number=1))     # 2.6185317999999995


