from re import template
from flask import render_template, url_for, request, redirect, session ,Blueprint
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required


admin = Blueprint('admin',__name__)

@admin.route('/admin/home', methods=["GET"])
@login_required
def home():
  return render_template('users/admin/home.html')
  

@admin.route('/admin/users/new', methods=["GET","POST"])
@login_required
def new_user():
  if request.method == "POST":
    print(dict(request.form))

    if 'admin' in request.form:
      user = User.create_admin(request.form)
      user.save()
    else:
      user = User.create_user(request.form)
      user.save()
  return render_template('users/admin/new_user.html')


@admin.route('/admin/users', methods=["GET"])
@login_required
def users():
  return render_template('users/admin/index.html', users=User.query.all())


@admin.route('/admin/users/edit/<integer:id>', methods=["POST", "GET"])
@login_required
def edit_user(id):
  user = User.query.filter_by(id=id).first_or_404()
  if request.method == "POST":
    pass