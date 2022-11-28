import os
import pytest
from src.core.logger import logger
from src.core.httprequest import HttpRequest


@pytest.fixture
def httprequest():
    request = HttpRequest(base_url=os.getenv("BASEURL"))
    return request
