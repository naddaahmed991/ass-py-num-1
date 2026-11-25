import threading


shared_counter = 0

lock = threading.Lock()


def increment_with_lock():
    global shared_counter

    for _ in range(10_000):

        with lock:
            shared_counter += 1


def run_with_lock():
    global shared_counter

    shared_counter = 0

    threads = []

    for _ in range(10):
        thread = threading.Thread(
            target=increment_with_lock
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("With Lock:", shared_counter)


run_with_lock()