''' create Notes class for user notes'''
from sqlalchemy import String, Integer, LargeBinary, Column, Table, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from base import Base, Session, engine
from user import User
from datetime import datetime

note_table = Table(
   'note', Base.metadata,
   Column('id', Integer, primary_key=True),
   Column('title', String(100), nullable=False),
   Column('description', String(500), nullable=False),
   Column('upload', LargeBinary),
   Column('created_at', DateTime),
   Column('updated_at', DateTime),
   Column('user_id', Integer, ForeignKey('user.id'))
)

class Notes(Base):
   __table__ = note_table
   user2 = relationship(User, back_populates="notes")

   def __init__(self, title, description, upload, created_at, updated_at, user):
       self.title = title
       self.description = description
       self.upload = upload
       self.created_at = created_at
       self.updated_at = updated_at
       self.user = user

   @classmethod
   def create(cls, title, description, upload, user):
       session = Session()
       note = cls(title=title, description=description, upload=upload, created_at=datetime.now(), updated_at=datetime.now(), user=user)
       session.add(note)
       session.commit()
       return note

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
