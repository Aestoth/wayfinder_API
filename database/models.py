from sqlalchemy import Column, Integer, String, Text
from database.db import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(120), unique=True, nullable=False)

    
    
class Layout(Base):
    __tablename__ = 'layout'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    floor = Column(String(50), nullable=False)
    
       

class Poi(Base):
    __tablename__ = 'pois'
    
    index = Column(Integer, primary_key=True)
    name = Column(Text(50), nullable=False)
    
    


class Path(Base):
    __tablename__ = 'paths'
    
    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    cost = Column(String(50), nullable=False)
    

Base.metadata.create_all(engine)