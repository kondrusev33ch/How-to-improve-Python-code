import time
from concurrent.futures import ProcessPoolExecutor, as_completed
# or you can import ThreadPoolExecutor for multithreading


# ---------------------------------------------------
def do_something(seconds):
    print('Start sleeping')
    time.sleep(seconds)
    return 'Done sleeping'


# ---------------------------------------------------
if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something, 1) for _ in range(20)]
        for f in as_completed(results):
            print(f.result())

        # Another example
        # secs = (5, 4, 3, 2, 1)
        # results = executor.map(do_something, secs)
        # for r in results:
        #     print(r)

    print(time.perf_counter())  # 2.3017665 sec
    # against 20.1 sec
