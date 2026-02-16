from flask import Blueprint,request
from services.dish_service import *
from utils.response import success,error

dish_bp=Blueprint("dishes",__name__,url_prefix="/api/v1")

@dish_bp.route("/restaurants/<int:rid>/dishes",methods=["POST"])
def add_dish(rid):
    data=request.json
    data["restaurant_id"]=rid
    return success(create_dish(data),201)

@dish_bp.route("/dishes/<int:did>",methods=["PUT"])
def update_dish_route(did):
    dish =update_dish(did,request.json)
    if dish:
        return success(dish)
    return error("Not found",404)

@dish_bp.route("/dishes/<int:did>/status",methods=["PUT"])
def change_status(did):
    dish=update_dish(did,request.json)
    if dish:
        return success({"message":"Status updated"})
    return error("Not found",404)


@dish_bp.route("/dishes/<int:did>",methods=["DELETE"])
def remove_dish(did):
    dish=delete_dish(did)
    if dish:
        return success({"message":"Dish Deleted"})
    return error("Not found",404)
