from home_password import db 

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)
  is_admin = db.Column(db.Boolean, unique=False, default=False)

  def save(self):
    db.session.add(self)
    db.session.commit(self)

  @classmethod
  def create_user(cls, arg):
    return cls(username=arg["username"], password=["password"])

  @classmethod
  def create_admin(cls, arg):
    return cls(username=arg["username"], password=["password"], is_admin=True)
    

  def __repr__(self):
    return f"Admin: {self.username}"

