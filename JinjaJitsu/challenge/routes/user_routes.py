from flask import Blueprint, render_template
from challenge.controllers.user_controller import greeting

home_routes = Blueprint('home', __name__)


home_routes.route('/', methods=['GET'])(greeting)

@home_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')