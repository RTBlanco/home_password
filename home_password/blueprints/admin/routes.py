from flask import render_template, url_for, request, redirect, session ,Blueprint, flash
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from home_password.blueprints.utils import admin_only


admin = Blueprint('admin',__name__)

@admin.route('/admin/home', methods=["GET","POST"])
@login_required
@admin_only
def home():
  return render_template('users/admin/home.html')
  

@admin.route('/admin/users/new', methods=["GET","POST"])
@login_required
def new_user():
  if request.method == "POST":
    print(dict(request.form))
    if User.query.filter_by(username=request.form["username"]).first() is None:
      if 'admin' in request.form:
        user = User.create_admin(request.form)
        user.save()
      else:
        user = User.create_user(request.form)
        user.save()

      user.add_sites(request.form.getlist('site'))
      user.save()
      return redirect("admin.home")
    flash("Username in database", "error")
  return render_template('users/admin/new_user.html', sites=Site.query.all())


@admin.route('/admin/users', methods=["GET"])
@login_required
def users():
  users = User.query.filter(User.id != current_user.id).all()
  return render_template('users/admin/index.html', users=users)


@admin.route('/admin/users/edit/<int:id>', methods=["POST", "GET"])
@login_required
def edit_user(id):
  user = User.query.filter_by(id=id).first_or_404()
  sites = Site.query.all()
  if request.method == "POST":
    print(dict(request.form))
    print(request.form.getlist('site'))
    if request.form["action"] == "Save":
      user.sites.clear()
      user.add_sites(request.form.getlist('site'))
      user.save()
  return render_template('users/admin/edit_user.html', user=user, sites=sites)
    