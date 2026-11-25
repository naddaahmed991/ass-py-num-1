import asyncio
import time


def heavy_cpu_function():
    result = 0

    for i in range(10_000_000):
        result += i * i

    return result


async def light_task():
    print("Light task: Start")

    await asyncio.sleep(1)

    print("Light task: Finish")


async def main():
    start_time = time.perf_counter()

    light = asyncio.create_task(light_task())

    print("Heavy CPU task: Start")

    result = heavy_cpu_function()

    print("Heavy CPU task: Finish")

    print(f"Result: {result}")

    await light

    end_time = time.perf_counter()

    print(f"Total time: {end_time - start_time:.2f} seconds")


asyncio.run(main())