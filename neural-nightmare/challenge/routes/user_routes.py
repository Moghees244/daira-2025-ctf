from flask import Blueprint, render_template
from challenge.controllers.user_controller import homepage, upload_file

home_routes = Blueprint('home', __name__)

home_routes.route('/', methods=['POST', 'GET'])(homepage)
home_routes.route('/uploads', methods=['POST', 'GET'])(upload_file)


@home_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')