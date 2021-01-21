from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from home_password.config import Config

# Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(Config)

  with app.app_context():
    db.init_app(app)
    # init_db()

  login_manager.init_app(app)
  bcrypt.init_app(app)

  # blueprint
  from home_password.blueprints.users.routes import users
  from home_password.blueprints.sites.routes import sites
  from home_password.blueprints.main.routes import main
  from home_password.blueprints.admin.routes import admin

  app.register_blueprint(users)
  app.register_blueprint(sites)
  app.register_blueprint(main)
  app.register_blueprint(admin)

  return app

def set_up():
  from home_password import create_app
  app = create_app()
  app.app_context().push()

  from home_password import db
  from home_password.models.user import User
  from home_password.models.site import Site
  return db, User, Site