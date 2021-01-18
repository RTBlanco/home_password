from home_password import app
from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site

@app.route('/')
@app.route('/login', methods=["GET",'POST'])
def login():
  print(dict(request.form))

  if request.method == "POST":
    user = User.query.filter_by(username=request.form["username"]).first()
    session["user_id"] = user.id
    return redirect(url_for('home'))

  return render_template('index.html')


@app.route('/home', methods=["GET"])
def home():
  if 'user_id' in session:
    return render_template('home.html', user=current_user())
  return "<h1>you are not logged in</h1>"


@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('login'))


@app.route('/sites', methods=["GET","POST"])
def sites():
  if "username" in session:
    print(dict(request.form))
    name = str(request.form.get('site_name', None))
    password = str(request.form.get('site_pw', None))
    return render_template("sites/index.html", name=name, password=password)
  return "<h1>you are not logged in</h1>"


@app.route('/sites/new', methods=["GET","POST"])
def new_site():
  if "username" in session:
    # print(dict(request.form))
    return render_template("sites/new.html")
  return "<h1>you are not logged in</h1>"

@app.route('/create_user', methods=["GET"])
def create_user():
  return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user_post():
  params = dict(request.form)
  user = User.create_admin(params)
  user.save()
  return render_template('create.html')

def current_user():
  return User.query.filter_by(id=session['user_id']).first()