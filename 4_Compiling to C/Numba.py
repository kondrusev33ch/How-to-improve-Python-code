from numba import jit
from timeit import timeit
import numpy as np
from functools import partial


@jit(nopython=True)
# ----------------------------------------------------
def function_nu(x=100000):
    result = 0
    for i in range(x):
        result += i
    return result


# ----------------------------------------------------
def function_py(x=100000):
    result = 0
    for i in range(x):
        result += i
    return result


@jit(nopython=True)
# ----------------------------------------------------
def fu_with_list(input_list):
    output_list = []
    for i in input_list:
        output_list.append(i * i)
    return output_list


@jit(nopython=True)
# ----------------------------------------------------
def fu_with_np_array(input_arr):
    output_list = []
    for i in input_arr:
        output_list.append(i * i)
    return output_list


# ----------------------------------------------------
if __name__ == '__main__':
    print(f'Numba:  {timeit(function_nu, number=1)}')  # slower because of compilation happened
    print(f'Python: {timeit(function_py, number=1)}')
    print(f'Numba:  {"%f" % timeit(function_nu, number=1)}')

    # Numba likes numpy but don't likes list
    # In this example you will get a warning about list using
    np_array = np.arange(100_000)
    normal_list = list(range(100_000))

    # compile first
    fu_with_list(normal_list)
    fu_with_np_array(np_array)

    print(f'Numba list arg:   {timeit(partial(fu_with_list, normal_list), number=1)}')
    print(f'Numba numpy arg:  {timeit(partial(fu_with_np_array, np_array), number=1)}')
