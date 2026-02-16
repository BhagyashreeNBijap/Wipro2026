from flask import Flask
from config import Config
from routes.restaurant_routes import restaurant_bp
from routes.dish_routes import dish_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(dish_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(order_bp)
    
    return app

app=create_app()

if __name__=="__main__":
    app.run()
