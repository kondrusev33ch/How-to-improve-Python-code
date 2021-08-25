import ctypes
from timeit import timeit

_libfib = ctypes.CDLL('D:\\Python\\High Performance\\4_Compiling to C\\Ctypes\\fib.so')


# ---------------------------------------------------
def python_fib(a=40):
    if a <= 0:
        return -1
    elif a == 1:
        return 0
    elif (a == 2) or (a == 3):
        return 1
    else:
        return python_fib(a - 2) + python_fib(a - 1)


# ---------------------------------------------------
def ctypes_fib(a=40):
    return _libfib.fib(ctypes.c_int(a))  # pay attention to data types!


# ---------------------------------------------------
if __name__ == '__main__':
    print(f'ctypes: {"%f" % timeit(ctypes_fib, number=1)}')  # => ctypes: 0.338805
    print(f'python: {"%f" % timeit(python_fib, number=1)}')  # => python: 15.992338

# Convert .c to .so:
# gcc -c -o fib.o fib.c
# gcc -shared -o fib.so fib.o
