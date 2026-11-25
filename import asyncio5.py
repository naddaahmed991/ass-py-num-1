import asyncio


async def cpu_task(task_name):
    print(f"{task_name}: Start")

    result = 0

    for i in range(5_000_000):
        result += i

        if i % 100_000 == 0:
            await asyncio.sleep(0)

    print(f"{task_name}: Finish")


async def main():
    await asyncio.gather(
        cpu_task("Task A"),
        cpu_task("Task B"),
    )


asyncio.run(main())