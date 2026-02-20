from flask import render_template, request

def homepage():
    return render_template('home.html')


def login_page():
    if request.method == 'TRACE':
        if 'X-Remote-Addr' in request.headers and request.headers['X-Remote-Addr'] == '127.0.0.1':
            return render_template('admin_panel.html', flag="THM{AlW@y$_d1s@Bl3_TRACE_1n_pr0ducT10n}")
        else:
            return render_template('error403.html', message = "Page is only accessible to local users")
    
    else:        
        if 'X-Remote-Addr' in request.headers and request.headers['X-Remote-Addr'] == '127.0.0.1':
            try:
                username = request.form['username']
                password = request.form['password']
            except KeyError:
                return render_template('login.html')

            if not username or not password:
                return render_template('login.html', message="Invalid Credentials")
        
            if username != "DumbDeveloper69" or password != "$h33my@pl@yboy.incakadumbdeveloper69":
                return render_template('login.html', message="Invalid Credentials")
        
            return render_template('admin_panel.html', flag="FSC{AlW@y$_d1s@Bl3_TRACE_1n_pr0ducT10n}")
        
        else:
            return render_template('error403.html', message = "Page is only accessible to local users")
        
