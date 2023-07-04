''' create Users class '''
from sqlalchemy import String, Integer, Column, Table, DateTime
from sqlalchemy.orm import relationship
from base import Base, Session, engine
from datetime import datetime

user_table = Table(
   'user', Base.metadata,
   Column('id', Integer, primary_key=True),
   Column('fname', String(50)),
   Column('lname', String(50)),
   Column('username', String(50), nullable=False),
   Column('password', String(50), nullable=False),
   Column('created_at', DateTime),
   Column('updated_at', DateTime),
)

class User(Base):
   __table__ = user_table
   credentials = relationship("Credentials", back_populates="user1")
   notes = relationship("Notes", back_populates="user2")

   def __init__(self, fname, lname, username, password, created_at, updated_at):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

   @classmethod
   def create(cls, fname, lname, username, password):
      session = Session()
      user = cls(fname=fname, lname=lname, username=username, password=password, created_at=datetime.now(), updated_at=datetime.now())
      session.add(user)
      session.commit()
      return user

   def update(self, **kwargs):
      session = Session()
      for key, value in kwargs.items():
          setattr(self, key, value)
      self.updated_at = datetime.now()
      session.commit()

   def delete(self):
      session = Session()
      session.delete(self)
      session.commit()

Base.metadata.create_all(engine)
