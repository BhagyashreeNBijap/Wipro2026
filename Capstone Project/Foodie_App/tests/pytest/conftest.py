import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def restaurant(base_url):
    payload = {
        "name": "Pytest Resto",
        "category": "Indian",
        "location": "Hyderabad",
        "contact": "9999999999"
    }
    response = requests.post(f"{base_url}/api/v1/restaurants", json=payload)
    assert response.status_code == 201
    return response.json()


@pytest.fixture(scope="session")
def user(base_url):
    payload = {
        "name": "Pytest User",
        "email": "pytest@test.com",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/api/v1/users/register", json=payload)
    assert response.status_code == 201
    return response.json()
