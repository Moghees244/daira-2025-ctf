import subprocess
from flask import render_template, request

def homepage():
    return render_template('home.html')

def process_data():
    if request.method == 'POST':
        message = request.form['message']

        valid, msg = valid_input(message)
        if not valid:
            return render_template('home.html', message = msg)

        command = f'echo {message};figlet {message}'
        output = subprocess.run(command, shell=True, capture_output=True, text=True)
        return render_template('home.html', message = output.stdout)
    
    if request.method == 'GET':
        return render_template('method_not_allowed.html')

def valid_input(message):
    blacklist_chars = [';', '&', '|', '&&', '||', '`', '\n', '\t', '<', '#']

    for character in blacklist_chars:
        if character in message:
            return False, "Malicious Input Detected! Be More Creative!!"
        
    blacklist_commands = ['cat', 'less', 'more', 'head', 'tail', 'id', 'whoami', 'uname', 'base64', 'echo', 'iconv', 'ls', ' ']
    for character in blacklist_commands:
        if f'$({character}' in message:
            return False, f"{character} Command is blacklisted. TRY HARDER!!!"
    
    return True, ''
