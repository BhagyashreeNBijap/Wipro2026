from flask import Flask, jsonify, request

app = Flask(__name__)

# -- Sample Data --
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    },
    {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 200
    }
]

bookings = []

# -- API ENDPOINTS --

# GET all movies
@app.route('/api/movies', methods=['GET'])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route('/api/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = None
    for m in movies:
        if m["id"] == movie_id:
            movie = m
            break
    if movie:
        return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# POST add a new movie
@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    if not data or "id" not in data or "movie_name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    # Check if movie ID already exists
    for m in movies:
        if m["id"] == data["id"]:
            return jsonify({"error": "Movie ID already exists"}), 400

    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route('/api/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = None
    for m in movies:
        if m["id"] == movie_id:
            movie = m
            break
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    data = request.get_json()
    movie.update(data)
    return jsonify(movie), 200

# DELETE movie
@app.route('/api/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    global movies
    movie = None
    for m in movies:
        if m["id"] == movie_id:
            movie = m
            break
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    movies = [m for m in movies if m["id"] != movie_id]
    return jsonify({"message": "Movie deleted"}), 200

# POST book tickets
@app.route('/api/bookings', methods=['POST'])
def book_ticket():
    data = request.get_json()
    if not data or "movie_id" not in data or "tickets" not in data:
        return jsonify({"error": "Invalid data"}), 400

    movie = None
    for m in movies:
        if m["id"] == data["movie_id"]:
            movie = m
            break
    if not movie:
        return jsonify({"error": "Movie not found"}), 404

    booking = {
        "booking_id": len(bookings) + 1,
        "movie_id": movie["id"],
        "movie_name": movie["movie_name"],
        "tickets": data["tickets"],
        "total_price": data["tickets"] * movie["price"]
    }
    bookings.append(booking)
    return jsonify(booking), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
