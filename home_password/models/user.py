from home_password import db, login_manager, bcrypt
from home_password.models import sites
from home_password.models.site import Site 
from flask_login import UserMixin
from flask import current_app


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

  def save(self):
    db.session.add(self)
    db.session.commit()

  def valid_login(self, password):
    """Checks if the password is correct
    the given instance"""
    return bcrypt.check_password_hash(self.password, password)

  def add_sites(self, list):
    """Takes in a list of site ids, finds them in the database
    and assigns them to the user """
    for site in list:
        self.sites.append(Site.query.filter_by(id=site).first())


  @classmethod
  def create_user(cls, arg):
    """ Creats a new Regular User Obj"""
    return cls(username=arg["username"], password=bcrypt.generate_password_hash(arg["password"]).decode('utf-8'))

  @classmethod
  def create_admin(cls, arg):
    """ Creats a new Admin User Obj"""
    return cls(username=arg["username"], password=bcrypt.generate_password_hash(arg["password"]).decode('utf-8'), is_admin=True)


  def __repr__(self):
    return f"User: {self.username}, {[i.id for i in self.sites]}"

