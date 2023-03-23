import pytest
from bs4 import BeautifulSoup
from django.test.client import Client as DjangoTestClient


class DjangoTestClientWithSelect(DjangoTestClient):
    def request(self, **request):
        response = super().request(**request)
        response.select = BeautifulSoup(response.content, "html5lib").select
        return response


@pytest.fixture
def client():
    return DjangoTestClientWithSelect()
