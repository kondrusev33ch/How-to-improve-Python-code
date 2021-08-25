import threading
import time


# ----------------------------------------------
def eat_breakfast():
    time.sleep(3)  # I/O pause
    print('You had breakfast')


# ----------------------------------------------
def go_poo():
    time.sleep(4)
    print('You pooped')


# ----------------------------------------------
def study():
    time.sleep(5)
    print('You finished studying')


# ----------------------------------------------
if __name__ == '__main__':

    eat_thread = threading.Thread(target=eat_breakfast)
    eat_thread.start()
    poop_thread = threading.Thread(target=go_poo)
    poop_thread.start()
    study_thread = threading.Thread(target=study)
    study_thread.start()

    print(threading.activeCount())  # how many threads are running
    print(threading.enumerate())

    eat_thread.join()
    poop_thread.join()
    study_thread.join()  # MainThread will wait for other 3 to execute

    print(time.perf_counter())  # time of the MainThread execution in seconds

    # Look at "concurrent_futures.py" for another method to do
    # multithreading or multiprocessing
