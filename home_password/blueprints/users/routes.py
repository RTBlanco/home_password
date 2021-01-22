from home_password.models.message import Message
from home_password.blueprints.main.routes import login
from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from flask import Blueprint
from home_password.blueprints.utils import user_only
from home_password import db

users = Blueprint('users', __name__)


@users.route('/home', methods=["GET","POST"])
@login_required
@user_only
def home():
  return render_template('users/regular/home.html')

@users.route("/<int:id>/sites", methods=["GET","POST"])
@login_required
def sites(id):
  if current_user == User.query.filter_by(id=id).first():
    return render_template("users/regular/sites.html", all_sites=current_user.sites)
  else:
    return redirect(url_for('users.home'))

@users.route('/users/message/admin', methods=["GET","POST"])
@login_required
def message():
  if request.method == "POST":
    # print(current_user.admin.username)
    admin = current_user.admin
    message = request.form["content"]
    current_user.send_msg(admin, message)
    current_user.save()
    return redirect(url_for('sites.site'))
  return render_template('users/regular/message.html')