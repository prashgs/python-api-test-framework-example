import requests
from urllib.parse import urljoin
import json
import requests


class HttpResponse:
    def __init__(self, response: requests.Response):
        if response:
            self.content = response.json()
            self.status = response.status_code
            self.description = response.reason