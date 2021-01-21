from home_password import db 

sites = db.Table('sites',
  db.Column('site_id', db.Integer, db.ForeignKey('site.id'), primary_key=True),
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

messages = db.Table('messages',
  db.Column('message_id', db.Integer, db.ForeignKey('message.id'), primary_key=True),
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)
