import timeit

# ----------------------------------------------------------
def fibonacci():
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


# We are encapsulating an infinite series of numbers into a function.
# This allows us to take as many values as we’d like from this stream and terminate
# when our code thinks it has had enough.

# “How many Fibonacci numbers below 5,000 are odd?”
# ----------------------------------------------------------
def fibonacci_naive():
    i, j = 0, 1
    count = 0
    while j <= 5000:
        if j % 2:
            count += 1
        i, j = j, i + j
    return count


# ----------------------------------------------------------
def fibonacci_transform():
    count = 0
    for f in fibonacci():
        if f > 5000:
            break
        if f % 2:
            count += 1
    return count


from itertools import takewhile


# ----------------------------------------------------------
def fibonacci_succinct():
    first_5000 = takewhile(lambda x: x <= 5000, fibonacci())
    return sum(1 for x in first_5000 if x % 2)

# All of these methods have similar runtime properties (as measured by their memory
# footprint and runtime performance), but the fibonacci_transform function benefits
# from several things. First, it is much more verbose than fibonacci_succinct, which
# means it will be easy for another developer to debug and understand.
