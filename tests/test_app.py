import pytest
from fastapi.testclient import TestClient

from bike_charts.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
