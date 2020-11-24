from app import db
from datetime import datetime

class Product(db.Model):
  __tablename__ = 'product'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(), nullable=True)
  price = db.Column(db.Integer, nullable=True)
  description = db.Column(db.String(), nullable=True)

  created_on = db.Column(db.DateTime(), default=datetime.now)
  updated_on = db.Column(db.DateTime(), default=datetime.now, onupdate=datetime.now)