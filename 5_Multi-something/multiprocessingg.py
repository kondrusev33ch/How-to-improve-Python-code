import time
from multiprocessing import Process


# ---------------------------------------------------
def do_something():
    print('Start sleeping')
    time.sleep(1)
    print('Done sleeping')


# ---------------------------------------------------
if __name__ == '__main__':

    # If you need to run multiple same processes,
    # ofc you may just write every process individually
    processes = []
    for _ in range(20):
        p = Process(target=do_something)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(time.perf_counter())  # => 1.3035755 sec
                                # against 20.1 sec
    # Look at "concurrent_futures.py" for another method to do
    # multithreading or multiprocessing
