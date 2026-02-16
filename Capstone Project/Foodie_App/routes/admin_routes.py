from flask import Blueprint
from models.restaurant_model import restaurants
from models.rating_model import ratings
from models.order_model import orders
from services.restaurant_service import update_restaurant
from utils.response import success, error

admin_bp = Blueprint("admin", __name__, url_prefix="/api/v1/admin")


@admin_bp.route("/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):
    restaurant = update_restaurant(rid, {"approved": True})
    if restaurant:
        return success({"message": "Approved"})
    return error("Not found", 404)


@admin_bp.route("/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    restaurant = update_restaurant(rid, {"disabled": True})
    if restaurant:
        return success({"message": "Disabled"})
    return error("Not found", 404)


@admin_bp.route("/feedback", methods=["GET"])
def view_feedback():
    return success(ratings)


@admin_bp.route("/orders", methods=["GET"])
def view_orders():
    return success(orders)
