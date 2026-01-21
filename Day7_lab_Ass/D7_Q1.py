'''#Question 1 – REST API Basics & Flask Server API introduction, HTTP verbs, REST principles, Building a simple Flask web server
Create a simple RESTful API using Flask that manages a list of users
. Requirements: 1. Create a Flask application GET /users → Return all users, GET /users/<id> → Return user details by ID, POST /users → Create a new user
3. Follow REST principles: Use proper HTTP status codes Return responses in JSON format
4. Store data in an in-memory list or dictionary'''

from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Bhagya"},
    {"id": 2, "name": "Sanvi"}
]

# GET /users → Return all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET /users/<id> → Return user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST /users → Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(debug=True,port=5002)
