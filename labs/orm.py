from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Password(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String, nullable=False)
    strength = Column(Integer, nullable=False)

def setup_database(database_path="sqlite:///passwords.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()