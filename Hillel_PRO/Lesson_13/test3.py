import asyncio
from time import perf_counter


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


# async def main():
#     start = perf_counter()
#     print("start")
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#     print("finish")
#     print(perf_counter() - start)

# asyncio.run(main())


async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    start = perf_counter()
    print("start")
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await asyncio.gather(task1, task2)
    print("finish")
    print(perf_counter() - start)


asyncio.run(main())
