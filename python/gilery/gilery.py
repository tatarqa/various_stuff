import sys
import time
import asyncio
import aiohttp



urls = [f'https://wikileaks.org/clinton-emails/emailid/{i}' for i in range(1,99999)]

async def fetch(url, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        try:
            start_time = time.perf_counter()
            async with session.get(url, allow_redirects=False, timeout=10) as response:
                end_time = time.perf_counter()
                if response.status == 200:
                        # TOU DOU
                    duration = (end_time - start_time) * 1000
                    return (url, duration)
                else:
                    return (url, -1)
        except Exception:
            return (url, -1)


async def main(loop):
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(fetch(url, loop)))
    await asyncio.gather(*tasks)
    results = map(lambda x: x.result(), tasks)
    for fetch_result in results:
        (url, result) = fetch_result
        print("{} ".format(url) + "{}ms".format(result))

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
