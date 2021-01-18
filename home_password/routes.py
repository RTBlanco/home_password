from home_password import app
from flask import render_template, url_for, request, redirect, session

@app.route('/')
@app.route('/login', methods=["GET",'POST'])
def login():
  print(dict(request.form))

  if request.method == "POST":
    session["username"] = request.form["username"]
    return redirect(url_for('home'))

  return render_template('index.html')


@app.route('/home', methods=["GET"])
def home():
  if 'username' in session:
    return render_template('home.html', username=session['username'])
  return "<h1>you are not logged in</h1>"


@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('login'))


@app.route('/sites', methods=["GET","POST"])
def sites():
  if "username" in session:
    return render_template("sites/index.html")
  return "<h1>you are not logged in</h1>"


@app.route('/sites/new', methods=["GET","POST"])
def new_site():
  if "username" in session:
    print(dict(request.form))
    return render_template("sites/new.html")
  return "<h1>you are not logged in</h1>"