from flask import render_template, url_for, request, redirect, session, flash
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import login_user, current_user, logout_user
from flask import Blueprint


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/login',  methods=["GET",'POST'])
def login():
  if request.method == "POST":
    user = User.query.filter_by(username=request.form["username"]).first()
    if user is not None and user.valid_login(request.form["password"]):
      login_user(user)
      if user.is_admin:
        return redirect(url_for('admin.home'))
      else:
        return redirect(url_for('users.home'))
    else:
      flash("incorrect login","error")
  return render_template('users/login.html')


@main.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.login'))