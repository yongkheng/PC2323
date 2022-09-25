import asyncio
import time
from asyncio import create_task

async def get_urls(arg):
    await asyncio.sleep(arg)
    print("retrieved all urls")

async def write_msg(arg):
    await asyncio.sleep(arg)
    print("write all to database")

async def main():
    #task1 = create_task(get_urls(3))
    #task2 = create_task(write_msg(2))
    tic = time.time()
    #await task1
    #await task2
    await asyncio.gather(get_urls(3), write_msg(2))
    toc = time.time()
    print(f"Elapsed: {toc-tic} s")

asyncio.run(main())
