from home_password import db 

class Site(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)

  def save(self):
    """Add the site to the 
    session and commits"""
    db.session.add(self)
    db.session.commit()

  def delete(self):
    """Deletes the Site and 
    then commits the change"""
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def create(cls, arg):
    """ Creats a new Regular User Obj"""
    return cls(name=arg["site_name"], password=arg["site_password"])

  def __repr__(self):
    return f"Site: {self.name}, {[i.id for i in self.users]}"
