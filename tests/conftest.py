import pytest
from fastapi.testclient import TestClient

from bike_charts.main import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)
