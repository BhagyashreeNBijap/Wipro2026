from flask import jsonify


def success(data, code=200):
    return jsonify(data), code


def error(message, code=400):
    return jsonify({"message": message}), code
