from array import array
import numpy as np
from timeit import timeit
from functools import partial


# -----------------------------------------------------
def norm_square_list(vector):
    norm = 0
    for v in vector:
        norm += v * v
    return norm


# -----------------------------------------------------
def norm_square_list_comprehension(vector):
    return sum([v * v for v in vector])


# -----------------------------------------------------
def norm_square_array(vector):
    norm = 0
    for v in vector:
        norm += v * v
    return norm


# -----------------------------------------------------
def norm_square_numpy(vector):
    return np.sum(vector * vector)  # similar to the loops from norm_square_list_comprehension()


# -----------------------------------------------------
def norm_square_numpy_dot(vector):
    return np.dot(vector, vector)


# -----------------------------------------------------
def list_create():
    return list(range(10_000_000))


# -----------------------------------------------------
def np_create():
    return np.arange(10_000_000)


# -----------------------------------------------------
if __name__ == '__main__':
    vec = list(range(1_000_000))
    print(f'norm_square_list:               '
          f'{timeit(partial(norm_square_list, vec), number=1)}')
    print(f'norm_square_list_comprehension: '
          f'{timeit(partial(norm_square_list_comprehension, vec), number=1)}')

    vec_arr = array('l', range(1_000_000))
    print(f'norm_square_array:              '
          f'{timeit(partial(norm_square_array, vec_arr), number=1)}')

    vec_np = np.arange(1_000_000)
    print(f'norm_square_numpy:              '
          f'{timeit(partial(norm_square_numpy, vec_np), number=1)}')
    print(f'norm_square_numpy_dot:          '
          f'{timeit(partial(norm_square_numpy_dot, vec_np), number=1)}')

    print(f'create_numpy: {timeit(np_create, number=1)}')
    print(f'create_list:  {timeit(list_create, number=1)}')

