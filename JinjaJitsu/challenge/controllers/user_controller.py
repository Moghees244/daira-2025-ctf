from flask import render_template_string, request

def greeting():
    user_input = request.args.get('name', '')
    template = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="public/css/login.css">
        <title>Jinja Jitsu</title>
      </head>
      <body>
        <div class="container">
          <h1>Jinja Jitsu</h1>
          <form action="/" method="get">
            <input type="text" name="name" placeholder="Enter your name here" />
            <button type="submit">Submit</button>
          </form>

          <h1>Hello {user_input}</h1>

        </div>
        <!-- Footer -->
        <div style="text-align: center;">
            <h3>Created By V0id</h3>
            <a href="https://www.linkedin.com/in/moghees-ahmad-064a94188" target="_blank"><b>LinkedIn</b></a>
            <a href="https://github.com/Moghees244" target="_blank"><b>Github</b></a>
        </div>
<!-- Footer -->
      </body>
    </html>
    """
    return render_template_string(template)