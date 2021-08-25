"""
pip install functools
"""

import time
from functools import wraps


# ---------------------------------------------------------------------------
def time_fn(fn):
    """Measures function execution time"""

    @wraps(fn)  # to save __name__, type(), ...
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f'@time_fn: {fn.__name__:20} took {t2 - t1} seconds')
        return result

    return measure_time


@time_fn
# ----------------------------------------------------------
def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


@time_fn
# ----------------------------------------------------------
def fn_terse(upper=1_000_000):
    return sum(range(upper))


# ----------------------------------------------------------
if __name__ == "__main__":
    assert fn_expressive() == fn_terse(), "Expect identical results from both functions"
