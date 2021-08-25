"""
pip install timeit
"""

import timeit


# ----------------------------------------------------------
def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


# ----------------------------------------------------------
def fn_terse(upper=1_000_000):
    return sum(range(upper))


# ----------------------------------------------------------
if __name__ == "__main__":
    print(timeit.timeit(fn_expressive, number=10))
    print(timeit.timeit(fn_terse, number=10))

    # or you can do this

    print('%f' % timeit.timeit("""a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]""", number=1000))  # create list
    print('%f' % timeit.timeit("""a=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)""", number=1000))  # create tuple
    # '%f' % for float, because it shows scientific
    # So you can pass everything to timeit

    # functions with arguments
    import functools
    arg = 1_000_000
    print(timeit.timeit(functools.partial(fn_terse, arg), number=10))

    # one more feature
    print(timeit.timeit('a=numpy.arange(100000)', setup='import numpy', number=1))

# timeit with console

# In[1]: %timeit a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 52.3 ns ± 0.111 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

# In[1]: %%timeit ...arguments...
# ...    expression
# Note that we use %%timeit instead of %timeit, which allows us to specify code to
# set up the experiment that doesn’t get timed.
