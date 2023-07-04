#!/usr/bin/env python3
''' create Notes class for user notes'''
from sqlalchemy import String, Integer, LargeBinary, Column, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('mysql://:localhost:3306/bilo_db')
class Notes:
   __table__ = 'notes'
   id =  Column(String)
   title = Column(String(100))
   description = Column(String(500))
   upload = Column(LargeBinary)