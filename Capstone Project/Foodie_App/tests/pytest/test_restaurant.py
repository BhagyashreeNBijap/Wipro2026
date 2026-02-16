import requests
import pytest
from jsonschema import validate

restaurant_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "category": {"type": "string"},
        "location": {"type": "string"},
        "contact": {"type": "string"},
        "approved": {"type": "boolean"},
        "disabled": {"type": "boolean"}
    },
    "required": ["id", "name", "approved", "disabled"]
}


def test_create_restaurant(base_url):
    payload = {
        "name": "Schema Resto",
        "category": "Chinese",
        "location": "Mumbai",
        "contact": "8888888888"
    }

    response = requests.post(f"{base_url}/api/v1/restaurants", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Schema Resto"

    validate(instance=data, schema=restaurant_schema)


@pytest.mark.parametrize("restaurant_id, expected_status", [
    (999, 404),
    (-1, 404),
])
def test_invalid_restaurant(base_url, restaurant_id, expected_status):
    response = requests.get(f"{base_url}/api/v1/restaurants/{restaurant_id}")
    assert response.status_code == expected_status
