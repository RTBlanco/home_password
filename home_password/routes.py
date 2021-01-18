from home_password import app
from flask import render_template, send_from_directory, url_for, request, redirect

@app.route('/')
def home():
  return "<h1>Home</h1>"