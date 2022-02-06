from sqlalchemy import Column, Integer, String
from database.db import *

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.name)
    
# SELECT * FROM students ORDER BY score DESC, course;
result = session.query(User) \
    .order_by(
        User.username.desc(),
).all()
    
    
class Layout(Base):
    __tablename__ = 'layout'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    floor = Column(String(50), nullable=False)
    
    def __repr__(self):
        return '<Layout %r>' % (self.name)
       

class Poi(Base):
    __tablename__ = 'pois'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    def __repr__(self):
        return '<Waypoint %r>' % (self.name)
    


class Path(Base):
    __tablename__ = 'paths'
    
    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    cost = Column(String(50), nullable=False)
    
    def __repr__(self):
        return '<Path %r>' % (self.name)
    

Base.metadata.create_all(engine)