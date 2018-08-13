from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here
Base = declarative_base()
# Example code:
class Volunteer(Base):
    __tablename__ = "volunteers"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    password = Column(String)
    location = Column(String)
    phone = Column(Integer)
    info = Column(String)
    elders = relationship("Elder", back_populates="volunteer")

    def __repr__(self):
        return ("Volunteer name: {}, Volunteer age: {}, Volunteer location: {}, Volunteer phone: {}, Volunteer info: {}".format(self.name, self.age, self.location, self.phone, self.info))

class Elder(Base):
    __tablename__ = "elders"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    location = Column(String)
    age = Column(Integer)
    phone = Column(Integer)
    info = Column(String)
    password = Column(String)
    volunteer_id = Column(Integer, ForeignKey(Volunteer.id))
    volunteer = relationship('Volunteer')

    def __repr__(self):
        return ("Elder name: {}, Elder location: {}, Elder phone: {}, Elder info: {}".format(self.name, self.location, self.phone, self.info))
