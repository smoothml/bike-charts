import falcon
import pytest
from falcon import testing

from bike_charts.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_default_response(client):
    response = client.simulate_get("/")

    assert response.status == falcon.HTTP_OK
    assert response.content == b"Hello, world!"
