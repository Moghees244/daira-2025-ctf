from flask import Blueprint, render_template
from challenge.controllers.user_controller import login_page, display_message

home_routes = Blueprint('home', __name__)


home_routes.route('/', methods=['GET', 'POST'])(login_page)
home_routes.route('/panel', methods=['GET'])(display_message)

@home_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')