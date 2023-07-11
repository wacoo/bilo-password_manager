from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base, engine
import datetime

class Credential(Base):
    __tablename__ = 'credentials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500))
    username = Column(String(50))
    password = Column(String(200))
    auto_fill = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_email = Column(String(50), ForeignKey('users.email'))
    user = relationship('User', backref='credentials')

    def __init__(self, url, username, password, auto_fill, user_email):
        self.url = url
        self.username = username
        self.password = password
        self.auto_fill = auto_fill
        self.user_email = user_email
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
Base.metadata.create_all(engine)