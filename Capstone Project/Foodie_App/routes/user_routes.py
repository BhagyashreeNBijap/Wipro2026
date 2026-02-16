from flask import Blueprint,request
from services.user_service import create_user
from services.rating_service import create_rating
from models.restaurant_model import restaurants
from utils.response import success,error

user_bp=Blueprint("users",__name__,url_prefix="/api/v1")

@user_bp.route("/users/register",methods=["POST"])
def register():
    return success(create_user(request.json),201)


@user_bp.route("/restaurants/search",methods=["GET"])
def search():
    return success(restaurants)

@user_bp.route("/ratings",methods=["POST"])
def rate():
    return success(create_rating(request.json),201)

