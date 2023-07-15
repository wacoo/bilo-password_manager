from sqlalchemy import Column, Integer, String, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
import datetime

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(1000))
    upload = Column(LargeBinary)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_email = Column(String(50), ForeignKey('users.email'))
    user = relationship('User', back_populates='notes')

    def __init__(self, description, upload, user_email):
        self.description = description
        self.upload = upload
        self.user_email = user_email
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()