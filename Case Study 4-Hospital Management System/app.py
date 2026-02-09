from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

patients = []

# Serve HTML file
@app.route("/")
def load_form():
    return send_from_directory(".", "patient_form.html")

# REST API

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200


@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json

    if not data or not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    patients.append(data)
    return jsonify({"message": "Patient registered"}), 201


@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    if pid >= len(patients):
        return jsonify({"error": "Patient not found"}), 404
    return jsonify(patients[pid]), 200


@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    if pid >= len(patients):
        return jsonify({"error": "Patient not found"}), 404

    patients[pid].update(request.json)
    return jsonify({"message": "Patient updated"}), 200


if __name__ == "__main__":
    app.run(debug=True)
