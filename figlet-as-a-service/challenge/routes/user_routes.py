from flask import Blueprint, render_template
from challenge.controllers.user_controller import homepage, process_data

home_routes = Blueprint('home', __name__)

home_routes.route('/', methods=['POST', 'GET'])(homepage)
home_routes.route('/data', methods=['POST', 'GET'])(process_data)


@home_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')