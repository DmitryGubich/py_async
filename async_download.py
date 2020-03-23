from time import time

import requests


def get_file(url):
    r = requests.get(url)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://avatars3.githubusercontent.com/u/18426280?s=400&u=e4c5ff457baceaad5c0ec08766cd59cd188b633f&v=4'
    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)


#################################################################

import asyncio
import aiohttp


def write_image(data):
    filename = f'file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url) as response:
        data = await response.read()
        write_image(data)


async def main2():
    url = 'https://avatars3.githubusercontent.com/u/18426280?s=400&u=e4c5ff457baceaad5c0ec08766cd59cd188b633f&v=4'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)
