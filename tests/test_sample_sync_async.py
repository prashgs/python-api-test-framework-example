import requests
import time
from random import randint
import asyncio
import pytest

base_url = 'https://pokeapi.co/api/v2/pokemon/'


def get_random_name():
    id = randint(1, 100)
    response = requests.get(f'{base_url}{id}')
    return response.json()['name']


async def get_random_name_async():
    return await asyncio.to_thread(get_random_name)


@pytest.mark.asyncio
async def test_sample_sync_async():
    tasks = []
    start_time = time.time()
    for _ in range(20):
        name = get_random_name()
        print(name)
    print("Sync: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    result = await asyncio.gather(*[asyncio.ensure_future(get_random_name_async()) for _ in range(20)])
    print(result)
    print("Async: --- %s seconds ---" % (time.time() - start_time))



