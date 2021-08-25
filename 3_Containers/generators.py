import timeit


# --------------------------------------------------------
def fibonacci_list(num_items):
    numbers = []
    a, b = 0, 1
    while len(numbers) < num_items:
        numbers.append(a)
        a, b = b, a + b
    return numbers


# --------------------------------------------------------
def fibonacci_gen(num_items):
    a, b = 0, 1
    while num_items:
        yield a
        a, b = b, a + b
        num_items -= 1


# --------------------------------------------------------
def t_fibonacci_list():
    for i in fibonacci_list(100_000):
        pass


# --------------------------------------------------------
def t_fibonacci_gen():
    for i in fibonacci_gen(100_000):
        pass


# --------------------------------------------------------
if __name__ == '__main__':
    print(f'list: {timeit.timeit(t_fibonacci_list, number=1)}')  # => 0.3229
    print(f'gen:  {timeit.timeit(t_fibonacci_gen, number=1)}')   # => 0.0960

    # %memit t_fibonacci_list()
    # peak memory: 448.61 MiB, increment: 397.10 MiB
    # %memit t_fibonacci_gen()
    # peak memory: 53.31 MiB, increment: 0.43 MiB
