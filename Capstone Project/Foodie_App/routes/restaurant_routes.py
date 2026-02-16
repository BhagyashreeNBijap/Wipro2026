from flask import Blueprint, request
from services.restaurant_service import *
from utils.response import success, error

restaurant_bp = Blueprint("restaurants", __name__, url_prefix="/api/v1/restaurants")


@restaurant_bp.route("", methods=["POST"])
def register_restaurant():
    return success(create_restaurant(request.json), 201)


@restaurant_bp.route("/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    restaurant = get_restaurant(rid)
    if restaurant:
        return success(restaurant)
    return error("Not found", 404)


@restaurant_bp.route("/<int:rid>",methods=["PUT"])
def update_restaurant_route(rid):
    restaurant=update_restaurant(rid,request.json)
    if restaurant:
        return success(restaurant)
    return error("Not found",404)

@restaurant_bp.route("/<int:rid>/disable",methods=["PUT"])
def disable_restaurant(rid):
    restaurant=update_restaurant(rid,{"disabled":True})
    if restaurant:
        return success({"message":"Restaurant disabled"})
    return error("Not found",404)
