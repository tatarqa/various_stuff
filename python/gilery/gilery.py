import sys
import time
import asyncio
import aiohttp
import os


#urls = [f'https://wikileaks.org/clinton-emails/emailid/{i}' for i in range(1,99999)]
urls = [
    f'https://wikileaks.org/clinton-emails/emailid/{i}' for i in range(2, 50)]


async def fetch(url, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        try:
            async with session.get(url, allow_redirects=False, timeout=10) as response:
                if response.status == 200:
                    responseDocument = await response.read()
                    return (url, responseDocument.decode('utf-8'))
                else:
                    return (url, -1)
        except Exception:
            return (url, -1)


async def main(loop):
    tasks = []
    outdir = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'htmlout')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for url in urls:
        tasks.append(asyncio.ensure_future(fetch(url, loop)))
    await asyncio.gather(*tasks)
    results = map(lambda x: x.result(), tasks)
    for i, fetch_result in enumerate(results):
        (url, responseDocument) = fetch_result
        with open(os.path.join(outdir, f'gilery{i}.html'), 'w') as htmlOutput:
            htmlOutput.write(responseDocument)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
