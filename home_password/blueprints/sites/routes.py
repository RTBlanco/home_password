from flask import render_template, url_for, request, redirect, session, Blueprint, flash
from home_password.models.site import Site
from flask_login import current_user, login_required
from home_password.blueprints.utils import admin_only

sites = Blueprint('sites', __name__)

@sites.route('/sites/new', methods=["GET", "POST"])
@login_required
@admin_only
def new_site():
  if request.method == "POST":
    site = Site.create(request.form)
    site.save()
    current_user.sites.append(site)
    current_user.save()
    return redirect(url_for('admin.home'))
  return render_template('sites/new.html')


@sites.route("/sites/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_only
def edit(id):
  site = Site.query.filter_by(id=id).first_or_404()
  if request.method == "POST":
    site.name = request.form["site_name"]
    site.password = request.form["site_password"]
    site.save()
    flash("Save successful", "success")
  return render_template("sites/edit.html", site=site)


@sites.route("/sites/delete/<int:id>", methods=["POST"])
@login_required
@admin_only
def delete(id):
  site = Site.query.filter_by(id=id).first_or_404()
  site.delete()
  flash("Site Deleted", "success")
  return redirect(url_for("sites.site"))
