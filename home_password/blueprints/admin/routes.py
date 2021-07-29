from home_password.blueprints.main.routes import login
from flask import render_template, url_for, request, redirect, session ,Blueprint, flash
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from home_password.blueprints.utils import admin_only
# from ipdb import set_trace


admin = Blueprint('admin',__name__)

@admin.route('/admin/home', methods=["GET","POST"])
@login_required
@admin_only
def home():
  users = [user for user in User.query.all() if user != current_user]
  return render_template('users/admin/home.html', sites=Site.query.all(), users=users)
  

@admin.route('/admin/users/edit/<int:id>', methods=["POST", "GET"])
@login_required
@admin_only
def edit_user(id):
  user = User.query.filter_by(id=id).first_or_404()
  sites = Site.query.all()
  if request.method == "POST":
    if 'user_type' in request.form and 'admin' == request.form["user_type"]:
      user.is_admin = True
    else:
      user.is_admin = False
    user.sites.clear()
    user.add_sites(request.form.getlist('site'))
    user.save() 
    flash("User Saved", "success")
  return render_template('users/admin/edit_user.html', user=user, sites=sites)
    

@admin.route("/admin/user/delete/<int:id>")
@login_required
@admin_only
def delete(id):
  user = User.query.filter_by(id=id).first_or_404()
  user.delete()
  flash("User Deleted", "success")
  return redirect(url_for("admin.home"))
