from flask import render_template, url_for, request, redirect, session, Blueprint
from home_password.models.site import Site
from flask_login import current_user, login_required

sites = Blueprint('sites', __name__)

@sites.route('/sites', methods=["GET"])
@login_required
def site():
  return render_template('sites/index.html', all_sites=Site.query.all())

@sites.route('/sites/new', methods=["GET", "POST"])
def new_site():
  if request.method == "POST":
    site = Site.create(request.form)
    site.save()
    return redirect(url_for('sites.site'))
  return render_template('sites/new.html')
