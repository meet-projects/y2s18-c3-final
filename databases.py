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
def add_volunteer(name,password, age, location, phone, info):
    print("Added a volunteer!")
    vol = Volunteer(name=name,password=password, age=age, location=location, phone=phone, info=info)
    session.add(vol)
    session.commit()

def add_elder(name,password,age, location, phone, info, volunteer_id):
    print("Added an elder!")
    elder = Elder(name=name,password=password,age=age, location=location, phone=phone, info=info, volunteer_id=volunteer_id)
    session.add(elder)
    session.commit()
def get_vol_by_name(name):
    volunteer = session.query(
    Volunteer).filter_by(
    name=name).first()
    return volunteer
def get_elder_by_name(name):
    elder = session.query(
    Elder).filter_by(
    name=name).first()
    return elder
def get_all_volunteers():
    vols = session.query(Volunteer).all()
    return vols

def get_all_elders():
    elders = session.query(Elder).all()
    return elders

def get_elder_by_location(loc):
    elders = session.query(Elder).filter_by(location=loc).all()
    return elders

def get_vol_by_elder(elder_id):
    elder = session.query(Elder).filter_by(id=elder_id).first()
    vol_id = elder.volunteer_id
    vol = session.query(Volunteer).filter_by(id=vol_id).first()
    return vol

def delete_all_vols():
	session.query(Volunteer).delete()
	session.commit()

def delete_all_elders():
	session.query(Elder).delete()
	session.commit()

def query_by_elder_name(name):
    elder=session.query(Elder).filter_by(name=name).first()
    return elder

#delete_all_elders()
# add_elder("Yosi", "jerusalem", 34545243, "my info", None)
# add_elder("Mordi", "jerusalem", 2221198, "my info", None)
# add_elder("Simon", "Nazareth", 9772113, "my info", None)

