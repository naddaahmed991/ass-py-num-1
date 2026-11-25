import threading
import time


shared_counter = 0


def increment_without_lock():
    global shared_counter

    for _ in range(10_000):
        temp = shared_counter

        time.sleep(0)

        shared_counter = temp + 1


def run_without_lock():
    global shared_counter

    shared_counter = 0

    threads = []

    for _ in range(10):
        thread = threading.Thread(
            target=increment_without_lock
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Without Lock:", shared_counter)


run_without_lock()