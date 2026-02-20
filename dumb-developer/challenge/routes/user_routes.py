from flask import Blueprint, render_template
from challenge.controllers.user_controller import homepage, login_page

home_routes = Blueprint('home', __name__)


home_routes.route('/', methods=['GET'])(homepage)
home_routes.route('/administrator-login-page', methods=['GET', 'POST', 'TRACE'])(login_page)


@home_routes.route('/<path:path>')
def handle_error(path):
    return render_template('error404.html')