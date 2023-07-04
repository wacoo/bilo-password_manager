from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/bilo_db', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()