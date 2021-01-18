from home_password import app
from flask import render_template, url_for, request, redirect

@app.route('/', methods=["GET",'POST'])
def home():
  print(dict(request.form))
  return render_template('index.html')