import aiohttp
import asyncio

async def test_connection(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.json())


async def main():
    num_con = 100
    url = 'http://161.35.153.209:5430/api/post?post_id=0'
    tasks = [test_connection(url) for i in range(num_con)]
    await asyncio.gather(*tasks)

asyncio.run(main())


