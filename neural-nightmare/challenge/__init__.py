import os
from flask import Flask
from .routes.user_routes import home_routes

def create_app():
    # Directory to store uploaded models
    UPLOAD_FOLDER = 'uploads/'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app = Flask(__name__, static_folder='public')

    app.register_blueprint(home_routes)
    return app