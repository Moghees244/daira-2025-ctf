from flask import Flask
from .routes.user_routes import home_routes

def create_app():
    app = Flask(__name__, static_folder='public')
    
    app.register_blueprint(home_routes)
    return app