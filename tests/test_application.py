import os
import re
import time

import pytest
from src.core.logger import logger


start_time = time.time()

@pytest.mark.asyncio
async def test_application(httprequest):
    logger.info(__name__)
    http_request = httprequest
    for number in range(0,3):
        response = await http_request.get_method(url_path='/products/1')
        print(response.content)

print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time))


        