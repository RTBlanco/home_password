from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import login_user, current_user, logout_user, login_required
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/')
@users.route('/login', methods=["GET",'POST'])
def login():
  if request.method == "POST":
    user = User.query.filter_by(username=request.form["username"]).first()
    if user is not None:
      login_user(user)
      return redirect(url_for('users.home'))

  return render_template('login.html')


@users.route('/home', methods=["GET"])
@login_required
def home():
  return render_template('home.html')
  

@users.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('users.login'))


@users.route('/user/new', methods=["GET","POST"])
@login_required
def new_user():
  if request.method == "POST":
    print(dict(request.form))

    if request.form["user_type"] == 'admin':
      user = User.create_admin(request.form)
      user.save()
    else:
      user = User.create_user(request.form)
      user.save()

  return render_template('users/new.html')