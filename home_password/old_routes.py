# from home_password import app
# from flask import render_template, url_for, request, redirect, session
# from home_password.models.user import User
# from home_password.models.site import Site
# from flask_login import login_user, current_user, logout_user, login_required



# @app.route('/')
# @app.route('/login', methods=["GET",'POST'])
# def login():


#   if request.method == "POST":
#     user = User.query.filter_by(username=request.form["username"]).first()
#     if user is not None:
#       login_user(user)
#       return redirect(url_for('home'))

#   return render_template('login.html')


# @app.route('/home', methods=["GET"])
# @login_required
# def home():
#   return render_template('home.html')
  

# @app.route('/logout')
# def logout():
#   # session.pop('username', None)
#   logout_user()
#   return redirect(url_for('login'))



# # def current_user():
# #   return User.query.filter_by(id=session['user_id']).first()
