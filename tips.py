import timeit
import functools


# ----------------------------------------------------------
# List creation
# ----------------------------------------------------------
def create_list_slow(val=100_000):
    li = []
    for i in range(val):
        li.append(i * 2)  # cause reallocating memory

    return li


def create_list_fast(val=100_000):
    return [i * 2 for i in range(val)]


print(f'create_list_slow: {timeit.timeit(create_list_slow, number=1)}')
print(f'create_list_fast: {timeit.timeit(create_list_fast, number=1)}')

# ----------------------------------------------------------
# Namespace lookups
# ----------------------------------------------------------
import math
from math import sin


def lookup1(x):
    res = 1
    for _ in range(1000):
        res += math.sin(x)
    return res


def lookup2(x):
    res = 1
    for _ in range(1000):
        res += sin(x)
    return res


def lookup3(x, sin=math.sin):
    res = 1
    for _ in range(1000):
        res += sin(x)
    return res


arg = 20
print(f'lookup1: {timeit.timeit(functools.partial(lookup1, arg), number=1)}')
print(f'lookup2: {timeit.timeit(functools.partial(lookup2, arg), number=1)}')
print(f'lookup3: {timeit.timeit(functools.partial(lookup3, arg), number=1)}')


# to get better understanding use dis module


# ----------------------------------------------------------
# Think before you do
# ----------------------------------------------------------
def loop_slow(num_iterations=10000):
    result = 0
    for i in range(num_iterations):
        result += i * sin(num_iterations)
    return result


def loop_fast(num_iterations=10000):
    result = 0
    for i in range(num_iterations):
        result += i
    return result * sin(num_iterations)


print(f'loop_slow: {timeit.timeit(loop_slow, number=1)}')
print(f'loop_fast: {timeit.timeit(loop_fast, number=1)}')


