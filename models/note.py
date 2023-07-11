from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, engine
import datetime

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    description = Column(String(1000))
    upload = Column(LargeBinary)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_email = Column(String(50), ForeignKey('users.email'))

    user = relationship('User', backref='notes')

    def __init__(self, title, description, upload, user_email):
        self.title = title
        self.description = description
        self.upload = upload
        self.user_email = user_email
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
Base.metadata.create_all(engine)