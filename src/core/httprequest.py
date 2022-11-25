import requests
from urllib.parse import urljoin


class HttpRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    def get_method(self, url_path: str = None, url_query_string: str = None) -> requests.Response:
        url = urljoin(url, url_path) if url_path else self.base_url
        url = urljoin(url, url_query_string) if url_query_string else url
        response = requests.get(url)
        return response

    def post_method(self, url_query_string, headers, payload):
        pass


x = HttpRequest("https://dummyjson.com/products/1")
print(x.get_method().content)
