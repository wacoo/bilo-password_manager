#!/usr/bin/env python3
''' create Users class '''
from sqlalchemy import String, Integer, LargeBinary, Column, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql://:localhost:3306/bilo_db')

class User:
   __table__ = 'users'
   id =  Column(String)
   fname = Column(String(50))
   lname = Column(String(50))
   username = Column(String(50))
   password = Column(String(50))

Base.metadata.create_all(engine)  
