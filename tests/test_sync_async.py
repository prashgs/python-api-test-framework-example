import asyncio
import time

import aiohttp
import pytest

from src.core.logger import logger

start_time = time.time()


@pytest.mark.asyncio
async def test_sync_async(httprequest):

    logger.info(__name__)
    tasks = []
    http_request = httprequest

    start_time = time.time()
    for number in range(1, 10):
        response = await http_request.get_method(url_path=f'/products/{number}')
        print(response.json()['title'])
    print("Sync: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    for number in range(1, 10):
        tasks.append(asyncio.ensure_future(
            http_request.get_method(url_path=f'/products/{number}')))
    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response.json()['title'])
    print("Async: --- %s seconds ---" % (time.time() - start_time))
