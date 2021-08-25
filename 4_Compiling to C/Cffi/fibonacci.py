from cffi import FFI, verifier
from timeit import timeit
from functools import partial

ffi = FFI()
ffi.cdef('int fib(int a);')

# lib = ffi.dlopen('D:\\Python\\High Performance\\4_Compiling to C\\Cffi\\fib.so')
# or
lib = ffi.verify(r"""
int fib(int a)
{
    if(a <= 0)
        return -1;
    else if (a == 1)
        return 0;
    else if ((a == 2) || (a == 3))
        return 1;
    else
        return fib(a - 2) + fib(a - 1);
}""")


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
if __name__ == '__main__':
    print(f'cffi:   {"%f" % timeit(partial(lib.fib, 40), number=1)}')  # => cffi:   0.296871
    print(f'python: {"%f" % timeit(python_fib, number=1)}')            # => python: 16.721654

# Convert .c to .so:
# gcc -c -o fib.o fib.c
# gcc -shared -o fib.so fib.o
