from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('mysql://root:root@localhost/bilo_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()