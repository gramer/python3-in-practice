import asyncio
import timeit
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import requests


class AsyncioPractice:

    def _fetch(self, url):
        response = requests.get(url)
        assert response.status_code == 200

    def processpool_fetch_all(self, urls):
        with ProcessPoolExecutor(max_workers=5) as executor:
            [executor.submit(self._fetch, url) for url in urls]

    def threadpool_fetch_all(self, urls):
        with ThreadPoolExecutor(max_workers=5) as executor:
            [executor.submit(self._fetch, url) for url in urls]

    def block_fetch_all(self, urls):
        [self._fetch(url) for url in urls]

    async def async_fetch(self, session, url):
        with aiohttp.Timeout(10):
            print('start:', url)
            async with session.get(url) as response:
                print('get urls:', url)
                assert response.status == 200

    async def async_fetch_all(self, session, urls):
        fetches = [asyncio.Task(self.async_fetch(session, url)) for url in urls]
        await asyncio.gather(*fetches)


if __name__ == '__main__':
    INPUT_URLS = [
        'http://b.ssut.me',
        'https://google.com',
        'https://apple.com',
        'https://ubit.info',
        'https://github.com/ssut'
    ]
    ASYNCIO_PRACTICE = AsyncioPractice()
    START = timeit.default_timer()
    LOOP = asyncio.get_event_loop()
    with aiohttp.ClientSession(loop=LOOP) as client_session:
        LOOP.run_until_complete(ASYNCIO_PRACTICE.async_fetch_all(client_session, INPUT_URLS))
    print(timeit.default_timer() - START)
