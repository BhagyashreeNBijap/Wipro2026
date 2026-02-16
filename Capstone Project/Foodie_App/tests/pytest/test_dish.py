import requests
from jsonschema import validate

dish_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "price": {"type": "number"},
        "enabled": {"type": "boolean"}
    },
    "required": ["id", "name", "enabled"]
}


def test_add_dish(base_url, restaurant):
    payload = {
        "name": "Biryani",
        "type": "Veg",
        "price": 200,
        "available_time": "12:00",
        "image": "b.jpg"
    }

    response = requests.post(
        f"{base_url}/api/v1/restaurants/{restaurant['id']}/dishes",
        json=payload
    )

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Biryani"

    validate(instance=data, schema=dish_schema)
