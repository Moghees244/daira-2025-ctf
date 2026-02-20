from flask import Flask
from .routes.user_routes import home_routes
from flask_jwt_extended import JWTManager
from .config import Config

def create_app():
    app = Flask(__name__, static_folder='public')
    jwt = JWTManager(app)
    
    app.config.from_object(Config)

    app.register_blueprint(home_routes)
    return app