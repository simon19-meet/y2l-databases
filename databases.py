from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,brand,rating):
  if price>300:
    print("Too Expensive")
  else:
    product=Product(name=name,price=price,brand=brand,rating=rating)
    session.add(product)
    session.commit()

def update_product(name,price,rating):
  if price>300:
    print("Too Expensive")
  else:
    product=session.query(Product).filter_by(name=name).first()
    product.price=price
    product.rating=rating
    session.commit()

def delete_product(name):
  session.query(Product).filter_by(name=name).delete()
  session.commit()

def get_product(id):
  pass
