import asyncio
import threading


shared_counter = 0

lock = threading.Lock()


def cpu_work():
    global shared_counter

    result = 0

    for i in range(1_000_000):
        result += i * i

    with lock:
        shared_counter += 1

    return result


async def async_task(task_number):
    print(f"Async Task {task_number}: Start")

    result = await asyncio.to_thread(cpu_work)

    print(f"Async Task {task_number}: Finish")

    return result


async def main():
    global shared_counter

    shared_counter = 0

    tasks = [
        async_task(i)
        for i in range(1, 9)
    ]

    results = await asyncio.gather(*tasks)

    print("Shared Counter:", shared_counter)

    print("Number of Results:", len(results))


asyncio.run(main())