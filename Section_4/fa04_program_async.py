import asyncio
import time

async def get_urls(arg):
    await asyncio.sleep(arg)
    print("retrieved all urls")

async def write_msg(arg):
    await asyncio.sleep(arg)
    print("write all to database")

async def main():
    tic = time.time()
    await asyncio.gather(
        get_urls(3),
        write_msg(2),
    )
    toc = time.time()
    print(f"Elapsed: {toc-tic} s")

asyncio.run(main())
