import time


# -------------------------------------------------------------------
def do_calculations(in_list):
    return [i * 2 for i in in_list]


# -------------------------------------------------------------------
if __name__ == '__main__':
    start = time.time()
    some_list = list(range(10_000_000))
    new_list = do_calculations(some_list)
    print(time.time() - start)


# 0.641669750213623
# 0.0558779239654541 with pypy

# I ran PyPy with console
