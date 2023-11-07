
import asyncio
import aiohttp
from datetime import datetime

async def coro_func():
    print("Hello, asyncio!")


async def async_sleep(num):
    print(f"sleeping {num} seconds")
    await asyncio.sleep(num)


async def scrape_page(session, url):
    print(f"Scraping {url}")
    async with session.get(url) as resp:
        return len(await resp.text())
    
    
async def main():
    # start = datetime.now()
    # coro_objs = []
    # for i in range(1, 4):
    #     coro_objs.append(async_sleep(i))

    # await asyncio.gather(*coro_objs
    #                    )
    # duration = datetime.now() - start
    # print(f"Took {duration.total_seconds():.2f} seconds.")
    urls = [
        "https://www.superdataminer.com/posts/66cff907ce8e",
        "https://www.superdataminer.com/posts/f21878c9897",
        "https://www.superdataminer.com/posts/b24dec228c43"
    ]

    coro_objs = []

    # using an aiohttp session to send http requests async
    # asyncio.gather() is needed to perform the requests in async
    async with aiohttp.ClientSession() as session:
        for url in urls:
            coro_objs.append(
                scrape_page(session, url)
            )
    
        results = await asyncio.gather(*coro_objs)

    for url, length in zip(urls, results):
        print(f"{url} -> {length}")

asyncio.run(main()) 