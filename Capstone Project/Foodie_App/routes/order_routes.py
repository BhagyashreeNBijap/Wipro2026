from flask import Blueprint, request
from services.order_service import create_order
from models.order_model import orders
from utils.response import success,error

order_bp=Blueprint("orders",__name__,url_prefix="/api/v1")

@order_bp.route("/orders",methods=["POST"])
def place_order():
    return success(create_order(request.json),201)


@order_bp.route("/restaurants/<int:rid>/orders",methods=["GET"])
def orders_by_restaurant(rid):
    return success([o for o in orders if o["restaurant_id"]==rid])


@order_bp.route("/users/<int:uid>/orders",methods=["GET"])
def orders_by_user(uid):
    return success([o for o in orders if o["user_id"]==uid])
