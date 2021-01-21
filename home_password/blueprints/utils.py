from flask_login import current_user
from flask import redirect,url_for
from functools import wraps

def admin_only(f):
    """ Checkes to see if the user is
    currently logged in is an admin, if not 
    it redirects to regular user homepage"""

    @wraps(f)
    def decorated_view(*args, **kwargs):
        if not current_user.is_admin:
            return redirect(url_for('users.home'))
        return f(*args, **kwargs)
    return decorated_view


def user_only(f):
    """ Checks to see if the user
    that is currenlty logged in is 
    a regular user, if not it redirects to the 
    admin homepage  """

    @wraps(f)
    def decorated_view(*args, **kwargs):
        if current_user.is_admin:
            return redirect(url_for('admin.home'))
        return f(*args, **kwargs)
    return decorated_view



