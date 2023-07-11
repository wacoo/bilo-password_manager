from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base, engine
import datetime

class User(Base):
    __tablename__ = 'users'
    fname = Column(String(50))
    lname = Column(String(50))
    email = Column(String(50), primary_key=True)
    password = Column(String(200))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
Base.metadata.create_all(engine)