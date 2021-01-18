from home_password import db, login_manager
from home_password.models import sites 
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)
  is_admin = db.Column(db.Boolean, unique=False, default=False)
  sites = db.relationship('Site', secondary=sites, lazy='subquery',
        backref=db.backref('users', lazy=True))

  @classmethod
  def create_user(cls, arg):
    return cls(username=arg["username"], password=["password"])

  @classmethod
  def create_admin(cls, arg):
    return cls(username=arg["username"], password=arg["password"], is_admin=True)


  def __repr__(self):
    return f"User: {self.username}, {[i.id for i in self.sites]}"

