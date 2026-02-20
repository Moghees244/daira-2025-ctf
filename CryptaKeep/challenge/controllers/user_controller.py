import os
from datetime import timedelta
from flask import render_template, request, url_for, redirect
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required

def login_page():
    try:
        username = request.form['username']
        password = request.form['password']

    except KeyError:
        return render_template('login.html')
    
    if not username or not password:
        return render_template('login.html', message="Invalid Credentials")

    if username == "dawg" or password == "password123":
        access_token = create_access_token(identity=username, expires_delta=timedelta(minutes=2))
        response = redirect(url_for('home.display_message', name='c4ca4238a0b923820dcc509a6f75849b.txt'))
        set_access_cookies(response, access_token)
    
    return response

@jwt_required()
def display_message():
    docs_folder = '../public/Documents'
    name = request.args.get('name')
    if not name:
        name = 'c4ca4238a0b923820dcc509a6f75849b.txt'

    return render_template('panel.html', pdf_path=os.path.join(docs_folder, name))
    