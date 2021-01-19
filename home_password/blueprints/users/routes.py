from flask import render_template, url_for, request, redirect, session
from home_password.models.user import User
from home_password.models.site import Site
from flask_login import current_user, login_required
from flask import Blueprint

users = Blueprint('users', __name__)


@users.route('/home', methods=["GET"])
@login_required
def home():
  return render_template('users/regular/home.html')
