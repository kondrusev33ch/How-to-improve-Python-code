import time
from joblib import Parallel, delayed


# ---------------------------------------------------
def do_something(secs):
    print('Start sleeping')
    time.sleep(1)
    return secs


# ---------------------------------------------------
if __name__ == '__main__':

    results = Parallel(n_jobs=20)(delayed(do_something)(i) for i in range(20))
    print(results)  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print(time.perf_counter())  # => 2.0925903 sec
                                # against 20.1 sec
