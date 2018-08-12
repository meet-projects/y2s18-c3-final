# Database related imports
# Make sure to import your tables!
from model import Base, Volunteer
from model import Base, Elder

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_volunteer(name, age, location, phone, info):
    print("Added a volunteer!")
    vol = Volunteer(name=name, age=age, location=location, phone=phone, info=info)
    session.add(vol)
    session.commit()

def add_elder(name, location, phone, info):
    print("Added an elder!")
    elder = Elder(name=name, location=location, phone=phone, info=info)
    session.add(elder)
    session.commit()

def get_all_volunteers():
    vols = session.query(Volunteer).all()
    return vols

def get_all_elders():
    elders = session.query(Elder).all()
    return elders

def get_elder_by_location(loc):
    elders = session.query(Elder).filter_by(location=loc).all()
    return elders

def get_vol_by_elder(id):
    vol = session.query(Elder).filter_by(volunteer_id=id).first()
    return vol