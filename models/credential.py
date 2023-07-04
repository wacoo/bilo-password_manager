#!/usr/bin/env python3
''' credential class '''
from sqlalchemy import Column, Integer, String, Boolean, create_engine, Table
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('mysql://root:root@localhost:3306/bilo_db', echo=True)
Session = sessionmaker(bind=engine)

credentials_table = Table(
    'credentials', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('url', String(50)),
    Column('username', String(50), nullable=False),
    Column('password', String(50), nullable=False),
    Column('owner', String(100), nullable=False),
    Column('auto_fill', Boolean, default=False)
)

class Credentials(Base):
    ''' Credential class for the credentials to be stored '''
    __table__ = credentials_table

    def generate_password(self, length, content):
        ''' generate password '''
        # implementation of password generation

Base.metadata.create_all(engine)