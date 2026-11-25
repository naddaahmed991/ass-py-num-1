import asyncio
import time


async def async_task(task_number):
    print(f"Task {task_number}: Start")

    await asyncio.sleep(1)

    print(f"Task {task_number}: Finish")


async def run_async_sequential():
    start_time = time.perf_counter()

    for i in range(1, 9):
        await async_task(i)

    end_time = time.perf_counter()

    print(f"Total execution time: {end_time - start_time:.2f} seconds")


asyncio.run(run_async_sequential())