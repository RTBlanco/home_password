from home_password import db 


class Site(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)

  def save(self):
    db.session.add(self)
    db.session.commit(self)

  def __repr__(self):
    return f"Site: {self.name}, {[i.id for i in self.users]}"
