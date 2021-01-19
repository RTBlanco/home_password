from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from flask import Blueprint

admin = Blueprint('admin',__name__)

@admin.route('/admin/home', methods=["GET"])
@login_required
def home():
  return render_template('users/admin/home.html')
  

@admin.route('/admin/new_user', methods=["GET","POST"])
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

  return render_template('users/admin/new_user.html')