import requests

def test_place_order(base_url, restaurant, user):
    # Add dish first
    dish_response = requests.post(
        f"{base_url}/api/v1/restaurants/{restaurant['id']}/dishes",
        json={
            "name": "Pizza",
            "type": "Veg",
            "price": 300,
            "available_time": "13:00",
            "image": "pizza.jpg"
        }
    )

    assert dish_response.status_code == 201
    dish_id = dish_response.json()["id"]

    # Place order
    order_response = requests.post(
        f"{base_url}/api/v1/orders",
        json={
            "user_id": user["id"],
            "restaurant_id": restaurant["id"],
            "dishes": [dish_id]
        }
    )

    assert order_response.status_code == 201
    assert order_response.json()["restaurant_id"] == restaurant["id"]
