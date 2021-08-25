import example_cy  # do not pay attention to this error
import example_py
from timeit import timeit
from functools import partial

# ----------------------------------------------
if __name__ == '__main__':
    arg = 100000
    print(f'Cython: {timeit(partial(example_cy.function, arg), number=1)}')
    print(f'Python: {timeit(partial(example_py.function, arg), number=1)}')

    # Output:
    # Cython: 0.00013489999999999336
    # Python: 0.03128510000000001

    # You can create html file
    # In console:
    # cython -a example_cy.pyx
