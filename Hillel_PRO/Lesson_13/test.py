import asyncio
import time
import requests
import aiohttp


async def blocking():
    response = requests.get("https://ukr.net")
    print(response.status_code)


async def async_http():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://ukr.net") as response:
            print(response.status)


async def main():
    await asyncio.gather(*(async_http() for _ in range(5)))


start = time.perf_counter()
asyncio.run(main())
print(time.perf_counter() - start)
