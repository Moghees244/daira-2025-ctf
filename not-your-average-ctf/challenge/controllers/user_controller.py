from flask import render_template, request

def login_page():
    if request.method == 'GET':
        return render_template('login.html')

    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return render_template('login.html', message="Invalid Credentials")

    if not username or not password:
        return render_template('login.html', message="Invalid Credentials")

    if username != "tyrellwellick@techinnovations.com" or password != "ll3ryT_8903":
        return render_template('login.html', message="Invalid Credentials")

    return render_template('admin_panel.html', flag="FCS{Th@ts_h0w_y0u_h@cK_pe0pl3}")