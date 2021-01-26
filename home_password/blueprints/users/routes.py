from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from flask import Blueprint, flash
from home_password.blueprints.utils import admin_only, user_only

users = Blueprint('users', __name__)


@users.route('/home', methods=["GET","POST"])
@login_required
@user_only
def home():
  return render_template('users/regular/home.html', sites=current_user.sites)


@users.route('/admin/users/new', methods=["GET","POST"])
@login_required
@admin_only
def new_user():
  if request.method == "POST":
    print(dict(request.form))
    if User.query.filter_by(username=request.form["username"]).first() is None:
      if 'admin' in request.form and 'admin' == request.form["user_type"]:
        user = User.create_admin(request.form)
        user.save()
      else:
        user = User.create_user(request.form)
        user.save()

      user.add_sites(request.form.getlist('site'))
      user.save()
      flash("User Created", "success")
      return redirect(url_for("admin.home"))
    flash("Username in database", "danger")
  return render_template('users/admin/new_user.html', sites=Site.query.all())