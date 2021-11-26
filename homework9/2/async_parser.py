import aiohttp
import asyncio
import time
import argparse


async def fetch(session, semaphore, url):
    async with semaphore:
        await session.get(url)


async def main(threads, file):
    tasks = []
    semaphore = asyncio.Semaphore(threads)
    async with aiohttp.ClientSession() as session:
        with open(file, 'r') as f:
            for url in f:
                task = asyncio.create_task(fetch(session, semaphore, url))
                tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int, default=10)
    parser.add_argument('-f', type=str, default='urls.txt')
    args = parser.parse_args()

    start = time.time()
    asyncio.run(main(args.c, args.f))
    end = time.time()

    print('Time - ', end - start)
