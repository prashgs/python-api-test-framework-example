import requests
from urllib.parse import urljoin
import json
from src.core.logger import logger

import asyncio

class HttpRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    async def get_method(self, url_path: str = None, url_query_string: str = None) -> requests.Response:
        logger.info(__name__)
        url = urljoin(self.base_url, url_path) if url_path else self.base_url
        url = urljoin(url, url_query_string) if url_query_string else url
        response = requests.get(url)
        return response

    async def post_method(self, headers: dict, payload: dict, url_path: str = None, url_query_string: str = None) -> requests.Response:
        logger.info(__name__)
        url = urljoin(self.base_url, url_path) if url_path else self.base_url
        url = urljoin(url, url_query_string) if url_query_string else url
        response = requests.post(url, headers=headers, json=payload)
        return response


# base_url = "https://dummyjson.com"

# x = HttpRequest(base_url=base_url)
# print(x.get_method(url_path='/products/1').content)

# payload = {'title': 'BMW Pencil'}
# headers = {'Content-Type': 'application/json'}
# print(x.post_method(url_path='/products/add',
#       headers=headers, payload=payload).content)
