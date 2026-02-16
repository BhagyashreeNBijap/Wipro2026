import requests
import pytest

def test_user_registration(base_url):
    payload = {
        "name": "New User",
        "email": "newuser@test.com",
        "password": "Bhagya@123"
    }

    response = requests.post(f"{base_url}/api/v1/users/register", json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "New User"


@pytest.mark.parametrize("invalid_payload", [
    {"email": "missingname@test.com"},
    {"name": "NoEmail"},
])
def test_invalid_user_registration(base_url, invalid_payload):
    response = requests.post(f"{base_url}/api/v1/users/register", json=invalid_payload)
    assert response.status_code == 400
