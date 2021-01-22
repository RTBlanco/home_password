from home_password import db 

class Message(db.Model):
  content = db.Column(db.String(30), unique=False, nullable=False)
  sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  recip_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  

  def save(self):
    """Add the message to the 
    session and commits"""
    db.session.add(self)
    db.session.commit()

  def delete(self):
    """Deletes the message and 
    then commits the change"""
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def create(cls, arg):
    """ Creats a new message Obj"""
    return cls(sender=arg["sender"], recip=arg["recip"], content=arg["content"])

  def __repr__(self):
    return f"Message:{self.content}"
