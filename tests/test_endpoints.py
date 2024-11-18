from fastapi.testclient import TestClient
from app.main import app
import pytest

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Poke-berries Statistics API"}


def test_all_berry_stats(client):
    response = client.get("/allBerryStats")
    assert response.status_code == 200
    data = response.json()
    assert "min_growth_time" in data
    assert "max_growth_time" in data
    assert "mean_growth_time" in data
    assert isinstance(data["min_growth_time"], int)
    assert isinstance(data["max_growth_time"], int)
    assert isinstance(data["mean_growth_time"], float)


def test_growth_times_are_valid(client):
    response = client.get("/allBerryStats")
    assert response.status_code == 200
    data = response.json()
    assert data["min_growth_time"] >= 0
    assert data["max_growth_time"] >= data["min_growth_time"]