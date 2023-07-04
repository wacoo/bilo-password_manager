''' credential class '''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from base import Base, Session, engine
from user import User
from datetime import datetime

credentials_table = Table(
    'credentials', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('url', String(50)),
    Column('username', String(50), nullable=False),
    Column('password', String(50), nullable=False),
    Column('owner', String(100), nullable=False),
    Column('auto_fill', Boolean, default=False),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('user_id', Integer, ForeignKey('user.id')),
)

class Credentials(Base):
    ''' Credential class for the credentials to be stored '''
    __table__ = credentials_table
    user1 = relationship(User, back_populates="credentials")

    def __init__(self, url, username, password, created_at, updated_at, user):
        self.url = url
        self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.user = user

    @classmethod
    def create(cls, url, username, password, user):
        session = Session()
        credential = cls(url=url, username=username, password=password, created_at=datetime.now(), updated_at=datetime.now(), user=user)
        session.add(credential)
        session.commit()
        return credential

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

    def generate_password(self, length, content):
        ''' generate password '''
        # implementation of password generation

Base.metadata.create_all(engine)
