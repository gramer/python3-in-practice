import asyncio

import aiohttp
import pytest

from practices.asyncio_practice import AsyncioPractice

asyncio_practice = AsyncioPractice()


def _urls():
    return ['http://b.ssut.me',
            'https://google.com',
            'https://apple.com',
            'https://ubit.info',
            'https://github.com/ssut'
            ]


@pytest.mark.benchmark(group="sync", warmup=True)
def test_async_fetch(benchmark):
    def _do():
        loop = asyncio.get_event_loop()
        with aiohttp.ClientSession(loop=loop) as session:
            loop.run_until_complete(asyncio_practice.async_fetch_all(session, _urls()))

    benchmark(_do)


@pytest.mark.benchmark(group="sync", warmup=True)
def test_block_fetch(benchmark):
    benchmark(lambda: asyncio_practice.block_fetch_all(_urls()))


@pytest.mark.benchmark(group="sync", warmup=True)
def test_threadpool_fetch(benchmark):
    benchmark(lambda: asyncio_practice.threadpool_fetch_all(_urls()))


@pytest.mark.benchmark(group="sync", warmup=True)
def test_processpool_fetch(benchmark):
    benchmark(lambda: asyncio_practice.processpool_fetch_all(_urls()))
