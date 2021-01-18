from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from home_password.config import Config

# Extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  login_manager.init_app(app)

  # blueprint
  from home_password.users.routes import users
  from home_password.sites.routes import sites
  from home_password.main.routes import main

  app.register_blueprint(users)
  app.register_blueprint(sites)
  app.register_blueprint(main)

  return app