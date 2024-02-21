from flask import redirect, session, request, url_for, flash, render_template
from .. import app


@app.route("/")
def index():
    if "user" in session:
        flash(f"{session['user']} logged in!")
        return render_template('index.html')
    flash("You aren't logged in!!!")
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['user'] = request.form.get('username')
        flash(f"User {session.get('user')} makes login...")
        return redirect(url_for("index"))
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''