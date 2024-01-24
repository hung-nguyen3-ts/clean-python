from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserORMModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    state = Column(String)