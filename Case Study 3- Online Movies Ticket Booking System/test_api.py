import requests
import pytest

BASE_URL = "http://127.0.0.1:5000/api"

# Fixtures
@pytest.fixture
def new_movie():
    return {
        "id": 103,
        "movie_name": "Tenet",
        "language": "English",
        "duration": "2h 30m",
        "price": 300
    }

# Test Cases
# Test GET all movies
def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Test GET movie by ID
def test_get_movie_by_id():
    response = requests.get(f"{BASE_URL}/movies/101")
    assert response.status_code == 200
    data = response.json()
    assert data["movie_name"] == "Interstellar"

# Test POST add a new movie
def test_add_movie(new_movie):
    response = requests.post(f"{BASE_URL}/movies", json=new_movie)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 103

# Test PUT update movie
def test_update_movie():
    update_data = {"price": 350}
    response = requests.put(f"{BASE_URL}/movies/103", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == 350

# Test DELETE movie
def test_delete_movie():
    response = requests.delete(f"{BASE_URL}/movies/103")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Movie deleted"

# Test POST booking tickets
def test_book_tickets():
    booking_data = {"movie_id": 101, "tickets": 2}
    response = requests.post(f"{BASE_URL}/bookings", json=booking_data)
    assert response.status_code == 201
    data = response.json()
    assert data["total_price"] == 500
